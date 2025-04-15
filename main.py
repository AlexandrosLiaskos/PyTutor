# main.py 
import os
import json
import sys
import subprocess 
from time import sleep

# Try importing rich, provide fallback if not installed
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.markdown import Markdown
    from rich.prompt import Prompt, IntPrompt, Confirm
    from rich.table import Table
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    # Basic fallback functions (keep as before)
    class Console:
        def print(self, *args, **kwargs): print(*args)
    console = Console()
    Panel = lambda text, **kwargs: console.print(f"\n--- {kwargs.get('title', '')} ---\n{text}\n-------------------\n")
    Syntax = lambda code, lexer, **kwargs: console.print(f"\n```python\n{code}\n```\n")
    Markdown = lambda text: console.print(text)
    # Added default="" to basic Prompt for compatibility with code input loop
    Prompt = lambda prompt, **kwargs: input(prompt + " ")
    IntPrompt = lambda prompt, **kwargs: int(input(prompt + " ")) # Add error handling
    Confirm = lambda prompt, **kwargs: input(prompt + " (y/n) ").lower().startswith('y')
    Table = lambda **kwargs: None # Fallback Table does nothing visually

# content.py might be reloaded if modified, but for now load once
try:
    from content import LESSON_CONTENT
except ImportError:
    console.print("[bold red]Error: Could not load content.py. Make sure it exists.[/bold red]")
    sys.exit(1)


PROGRESS_FILE = "progress.json"

# --- Progress Functions (keep as before) ---
def load_progress():
    """Loads user progress from the JSON file."""
    try:
        with open(PROGRESS_FILE, 'r') as f:
            # Ensure default structure if file exists but is empty/invalid
            data = json.load(f)
            if "completed_lessons" not in data:
                data["completed_lessons"] = []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"completed_lessons": []} # Default structure

def save_progress(progress_data):
    """Saves user progress to the JSON file."""
    try:
        # Ensure the key exists before saving
        if "completed_lessons" not in progress_data:
            progress_data["completed_lessons"] = []
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress_data, f, indent=4)
    except IOError as e:
        console.print(f"[bold red]Error saving progress:[/bold red] {e}")
    except TypeError as e:
        console.print(f"[bold red]Error encoding progress data (check content):[/bold red] {e}")


# --- UI Functions (mostly unchanged, adjusted display_module_selection table) ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    clear_screen()
    if RICH_AVAILABLE:
        console.print(Panel("[bold cyan]Welcome to the Interactive Python Terminal Tutor![/bold cyan]",
                            title="PyTutor", border_style="blue"))
    else:
        console.print("\n--- PyTutor ---\nWelcome to the Interactive Python Terminal Tutor!\n-------------------\n")
    console.print("Learn Python step-by-step, right here in your terminal.")
    sleep(1.5)

def display_main_menu(progress_data):
    # Use Panel if rich is available for better framing
    if RICH_AVAILABLE:
        menu_panel_content = "[bold yellow]Main Menu:[/bold yellow]\n"
        menu_panel_content += "1. Start/Continue Learning\n"
        menu_panel_content += "2. View Progress\n"
        menu_panel_content += "3. Reset Progress\n"
        menu_panel_content += "4. Exit"
        console.print(Panel(menu_panel_content, title="Menu", border_style="blue", expand=False))
        options = {"1": ..., "2": ..., "3": ..., "4": ...} # Used only for choice validation
    else:
        console.print("\nMain Menu:")
        options = {
            "1": "Start/Continue Learning",
            "2": "View Progress",
            "3": "Reset Progress",
            "4": "Exit"
        }
        for key, value in options.items():
            console.print(f"{key}. {value}")

    # Use IntPrompt for choice validation regardless of rich
    try:
        choice = IntPrompt.ask("[cyan]Choose an option[/cyan]", choices=list(options.keys()))
        return choice
    except ValueError:
         console.print("[bold red]Invalid input. Please enter a number.[/bold red]")
         sleep(1.5)
         return None # Indicate invalid choice

def display_module_selection(progress_data):
    clear_screen()
    if RICH_AVAILABLE:
        console.print(Panel("[bold green]Select a Module[/bold green]", border_style="green"))
    else:
         console.print("\n--- Select a Module ---\n")

    completed_lessons = progress_data.get("completed_lessons", [])

    table = None
    if RICH_AVAILABLE:
        table = Table(title="Modules", show_header=True, header_style="bold magenta", expand=False)
        # Adjust column widths if needed
        table.add_column("No.", style="dim", width=5, justify="right")
        table.add_column("Module Title", style="cyan", min_width=20, no_wrap=False) # Allow wrapping
        table.add_column("Status", style="yellow", width=15, justify="center") # Fixed width for status

    module_options = {}
    if not LESSON_CONTENT:
        console.print("[italic]No modules available yet.[/italic]")
    else:
        for i, module in enumerate(LESSON_CONTENT):
            module_id = module.get("id", f"mod_{i}") # Use ID if available
            module_lessons = {lesson['id'] for lesson in module.get('lessons', [])} # Safer access
            total_in_module = len(module_lessons)
            completed_in_module = [l_id for l_id in completed_lessons if l_id in module_lessons]
            status_text = ""

            if total_in_module == 0:
                 status_text = "[dim]No Lessons[/dim]"
            elif len(completed_in_module) == total_in_module:
                 status_text = "[bold green]Completed[/bold green]"
            elif len(completed_in_module) > 0:
                 status_text = f"[bold yellow]{len(completed_in_module)}/{total_in_module}[/bold yellow]"
            else:
                 status_text = "[dim]Not Started[/dim]"

            option_num = str(i + 1)
            module_options[option_num] = module # Store the module itself

            if RICH_AVAILABLE and table is not None:
                 # Ensure module title exists
                 table.add_row(option_num, module.get('title', f'Module {i+1}'), status_text)
            else:
                 # Fallback display
                 status_plain = status_text.replace("[bold green]","").replace("[/bold green]","").replace("[bold yellow]","").replace("[/bold yellow]","").replace("[dim]","").replace("[/dim]","")
                 console.print(f"{option_num}. {module.get('title', f'Module {i+1}')} ({status_plain})")

    if RICH_AVAILABLE and table is not None and table.row_count > 0:
        console.print(table)
    elif not RICH_AVAILABLE and not module_options:
        pass # Message already printed if LESSON_CONTENT is empty

    console.print("\n0. Back to Main Menu")
    module_options["0"] = None # Back option

    choices = list(module_options.keys())
    if not choices: # No modules + back option
        return None # Should not happen if LESSON_CONTENT is empty check works

    chosen_num = Prompt.ask("[cyan]Choose a module number (or 0 to go back)[/cyan]", choices=choices)

    return module_options.get(chosen_num) # Return selected module or None

def display_lesson_selection(module, progress_data):
    clear_screen()
    module_title = module.get('title', 'Unnamed Module') # Safer access
    if RICH_AVAILABLE:
        console.print(Panel(f"[bold green]Module: {module_title}[/bold green]", border_style="green"))
    else:
        console.print(f"\n--- Module: {module_title} ---\n")

    completed = progress_data.get("completed_lessons", [])
    lessons = module.get('lessons', []) # Safer access

    console.print("[bold yellow]Lessons:[/bold yellow]")
    lesson_options = {}
    if not lessons:
        console.print("[italic]No lessons in this module yet.[/italic]")
    else:
        for i, lesson in enumerate(lessons):
            lesson_id = lesson.get('id', f"lesson_{i}") # Safer access
            lesson_title = lesson.get('title', f"Lesson {i+1}") # Safer access
            status = "[bold green]✓[/bold green]" if lesson_id in completed else "[dim]○[/dim]"
            option_num = str(i + 1)
            lesson_options[option_num] = lesson
            console.print(f"{option_num}. {lesson_title} {status}")

    console.print("\n0. Back to Module Selection")
    lesson_options["0"] = None

    choices = list(lesson_options.keys())
    if not choices:
        return None # Should not happen

    chosen_num = Prompt.ask("[cyan]Choose a lesson number (or 0 to go back)[/cyan]", choices=choices)

    return lesson_options.get(chosen_num)

# --- Lesson Execution (MODIFIED with 'code' type) ---
def run_lesson(lesson, progress_data):
    """Displays and handles a single lesson. Returns False on critical errors."""
    clear_screen()
    lesson_title = lesson.get('title', 'Unnamed Lesson') # Safer access
    if RICH_AVAILABLE:
        console.print(Panel(f"[bold magenta]Lesson: {lesson_title}[/bold magenta]", border_style="magenta", expand=False))
    else:
        console.print(f"\n--- Lesson: {lesson_title} ---\n")


    lesson_id = lesson.get('id')
    lesson_type = lesson.get('type')

    if not lesson_id or not lesson_type:
        console.print("[bold red]Error: Lesson is missing 'id' or 'type'.[/bold red]")
        sleep(2)
        return True # Continue, but skip lesson


    # --- Explanation Type ---
    if lesson_type == 'explanation':
        if lesson.get('text'):
            for line in lesson['text']:
                if RICH_AVAILABLE:
                    console.print(Markdown(line), highlight=False)
                else:
                    console.print(line) # Basic print for fallback
        if lesson.get('example'):
            console.print("\n[bold]Example:[/bold]" if RICH_AVAILABLE else "\nExample:")
            if RICH_AVAILABLE:
                syntax = Syntax(lesson['example'], "python", theme="default", line_numbers=True)
                console.print(syntax)
            else:
                 console.print(f"```python\n{lesson['example']}\n```") # Basic code block fallback

        # Mark as completed after viewing
        if lesson_id not in progress_data.get('completed_lessons', []):
             # Ensure list exists before appending
             if 'completed_lessons' not in progress_data:
                 progress_data['completed_lessons'] = []
             progress_data['completed_lessons'].append(lesson_id)
             save_progress(progress_data)
             console.print("\n[bold green]Lesson viewed and marked as completed![/bold green]" if RICH_AVAILABLE else "\nLesson viewed and marked as completed!")
        else:
             console.print("\n[dim]Lesson previously completed.[/dim]" if RICH_AVAILABLE else "\nLesson previously completed.")

        # Use basic input if Prompt fails or rich is not available
        try:
            Prompt.ask("\n[cyan]Press Enter to continue...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to continue...")
        except Exception:
             input("\nPress Enter to continue...")


    # --- Quiz Type ---
    elif lesson_type == 'quiz':
        question = lesson.get('question', 'No question provided.')
        options = lesson.get('options', [])
        correct_answer_index = lesson.get('correct_answer') # Keep as index

        if not options or correct_answer_index is None:
             console.print("[bold red]Error: Quiz lesson is missing 'options' or 'correct_answer'.[/bold red]")
             sleep(2)
             return True # Skip lesson

        if RICH_AVAILABLE:
            console.print(Markdown(f"**Question:** {question}"), highlight=False)
            console.print("\n[bold]Options:[/bold]")
        else:
            console.print(f"\nQuestion: {question}")
            console.print("\nOptions:")

        choices_map = {}
        for i, option in enumerate(options):
            choice_num = str(i + 1)
            choices_map[choice_num] = i # Map display number to 0-based index
            console.print(f"{choice_num}. {option}")

        try:
             # Use Prompt with choices for validation
             user_answer_num = Prompt.ask("\n[cyan]Your answer (number)[/cyan]" if RICH_AVAILABLE else "\nYour answer (number)", choices=list(choices_map.keys()))
             user_answer_index = choices_map[user_answer_num]

             if user_answer_index == correct_answer_index:
                console.print("\n[bold green]Correct! 🎉[/bold green]" if RICH_AVAILABLE else "\nCorrect!")
                if lesson_id not in progress_data.get('completed_lessons', []):
                    if 'completed_lessons' not in progress_data:
                        progress_data['completed_lessons'] = []
                    progress_data['completed_lessons'].append(lesson_id)
                    save_progress(progress_data)
                    console.print("[italic]Lesson marked as completed![/italic]" if RICH_AVAILABLE else "Lesson marked as completed!")
                sleep(1.5)
             else:
                correct_num_display = correct_answer_index + 1
                correct_text = options[correct_answer_index]
                console.print(f"\n[bold red]Incorrect.[/bold red] The correct answer was: {correct_num_display}. {correct_text}" if RICH_AVAILABLE else f"\nIncorrect. The correct answer was: {correct_num_display}. {correct_text}")
                sleep(2)

        except (ValueError, KeyError):
             console.print("[bold red]Invalid choice.[/bold red]" if RICH_AVAILABLE else "Invalid choice.")
             sleep(1.5)
        finally:
             # Ensure continue prompt appears even on error
             try:
                 Prompt.ask("\n[cyan]Press Enter to continue...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to continue...")
             except Exception:
                 input("\nPress Enter to continue...")


    # --- Code Challenge Type (NEW) ---
    elif lesson_type == 'code':
        # 1. Display Explanation (if any)
        explanation = lesson.get('explanation')
        if explanation and isinstance(explanation, list):
             if RICH_AVAILABLE:
                 console.print(Markdown("**Concept:**"), highlight=False)
                 for line in explanation:
                     console.print(Markdown(f"- {line}"), highlight=False)
             else:
                 console.print("\nConcept:")
                 for line in explanation:
                     console.print(f"- {line}")
             console.print("-" * 20)

        # 2. Display Challenge
        challenge = lesson.get('challenge')
        if challenge and isinstance(challenge, list):
            if RICH_AVAILABLE:
                console.print(Markdown("**Challenge:**"), highlight=False)
                for line in challenge:
                     console.print(f"- {line}") # Keep challenge lines plain
            else:
                console.print("\nChallenge:")
                for line in challenge:
                     console.print(f"- {line}")
        else:
            console.print("[yellow]Warning: No challenge text found for this coding lesson.[/yellow]" if RICH_AVAILABLE else "Warning: No challenge text found for this coding lesson.")
            try: Prompt.ask("\n[cyan]Press Enter to continue...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to continue...")
            except Exception: input("\nPress Enter to continue...")
            return True # Exit lesson if no challenge defined

        # 3. Get User Code Input
        console.print("\n[yellow]Enter your Python code below. Type '[bold]RUN[/bold]' on a new line when finished:[/yellow]" if RICH_AVAILABLE else "\nEnter your Python code below. Type 'RUN' on a new line when finished:")
        user_code_lines = []
        while True:
            try:
                # Use basic input for multiline, Prompt isn't ideal here
                line = input("> ")
                if line.strip().upper() == 'RUN':
                    break
                user_code_lines.append(line)
            except EOFError: # Handle Ctrl+D
                 console.print("\n[yellow]Input cancelled.[/yellow]" if RICH_AVAILABLE else "\nInput cancelled.")
                 break # Treat as skipping execution
            except KeyboardInterrupt: # Handle Ctrl+C
                 console.print("\n[yellow]Input interrupted.[/yellow]" if RICH_AVAILABLE else "\nInput interrupted.")
                 return True # Exit lesson flow, maybe prompt to retry? For now, just continue.

        user_code = "\n".join(user_code_lines)

        if not user_code.strip():
            console.print("[yellow]No code entered. Skipping execution.[/yellow]" if RICH_AVAILABLE else "No code entered. Skipping execution.")
            try: Prompt.ask("\n[cyan]Press Enter to continue...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to continue...")
            except Exception: input("\nPress Enter to continue...")
            return True

        # 4. Execute Code and Check Output
        console.print("\n[dim]Running your code...[/dim]" if RICH_AVAILABLE else "\nRunning your code...")
        sleep(0.5)
        expected_stdout = lesson.get('expected_stdout', None)

        # If no expected output, just run the code for practice without checking/completion
        if expected_stdout is None:
             console.print("[yellow]Warning: No expected output defined. Running code for practice.[/yellow]" if RICH_AVAILABLE else "Warning: No expected output defined. Running code for practice.")
             try:
                 # Still run it to show errors if any
                 result = subprocess.run(
                     [sys.executable or 'python', '-c', user_code],
                     capture_output=True,
                     text=True,
                     timeout=5 # 5-second timeout
                 )
                 stderr = result.stderr.strip()
                 console.print("-" * 20)
                 if stderr:
                     console.print("[bold red]Error during execution:[/bold red]" if RICH_AVAILABLE else "Error during execution:")
                     if RICH_AVAILABLE: console.print(Panel(stderr, style="red", border_style="red", title="Error Output"))
                     else: console.print(f"--- Error Output ---\n{stderr}\n------------------")
                 else:
                     console.print("[bold blue]Code executed (no verification needed).[/bold blue]" if RICH_AVAILABLE else "Code executed (no verification needed).")
                     output_title = "Your Output"
                     output_content = result.stdout if result.stdout.strip() else "[No Output]"
                     if RICH_AVAILABLE: console.print(Panel(output_content, style="blue", border_style="blue", title=output_title))
                     else: console.print(f"--- {output_title} ---\n{output_content}\n---------------")

             except subprocess.TimeoutExpired:
                 console.print("[bold red]Error: Your code took too long to execute (Timeout).[/bold red]" if RICH_AVAILABLE else "Error: Your code took too long to execute (Timeout).")
                 console.print("[dim]Check for infinite loops or very long operations.[/dim]" if RICH_AVAILABLE else "Check for infinite loops or very long operations.")
             except FileNotFoundError:
                  python_exe = sys.executable or 'python'
                  console.print(f"[bold red]Error: Could not find Python interpreter ('{python_exe}'). Is it in your PATH?[/bold red]" if RICH_AVAILABLE else f"Error: Could not find Python interpreter ('{python_exe}'). Is it in your PATH?")
                  sleep(3)
                  return False # Indicate critical failure
             except Exception as e:
                 console.print(f"[bold red]An unexpected error occurred during execution:[/bold red] {e}" if RICH_AVAILABLE else f"An unexpected error occurred during execution: {e}")
             finally:
                 try: Prompt.ask("\n[cyan]Press Enter to continue...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to continue...")
                 except Exception: input("\nPress Enter to continue...")
             return True # Continue to next lesson even if execution failed (practice)


        # --- Code Verification Logic ---
        try:
            result = subprocess.run(
                [sys.executable or 'python', '-c', user_code], # Use sys.executable
                capture_output=True,
                text=True,
                timeout=5 # 5-second timeout
            )

            # Normalize stdout (strip trailing whitespace, ensure single trailing newline)
            actual_stdout_raw = result.stdout or ""
            actual_stdout = actual_stdout_raw.rstrip().replace('\r\n', '\n') + '\n'

            # Normalize expected output similarly
            normalized_expected = expected_stdout.rstrip().replace('\r\n', '\n') + '\n'

            stderr = result.stderr.strip()

            console.print("-" * 20) # Separator
            success = False
            if stderr:
                console.print("[bold red]Error during execution:[/bold red]" if RICH_AVAILABLE else "Error during execution:")
                if RICH_AVAILABLE: console.print(Panel(stderr, style="red", border_style="red", title="Error Output"))
                else: console.print(f"--- Error Output ---\n{stderr}\n------------------")
            elif actual_stdout == normalized_expected:
                console.print("[bold green]Correct! Your code produced the expected output. 🎉[/bold green]" if RICH_AVAILABLE else "Correct! Your code produced the expected output.")
                output_title = "Your Output"
                output_content = actual_stdout_raw if actual_stdout_raw.strip() else "[No Output]"
                if RICH_AVAILABLE: console.print(Panel(output_content, style="green", border_style="green", title=output_title))
                else: console.print(f"--- {output_title} ---\n{output_content}\n---------------")

                if lesson_id not in progress_data.get('completed_lessons', []):
                    if 'completed_lessons' not in progress_data:
                        progress_data['completed_lessons'] = []
                    progress_data['completed_lessons'].append(lesson_id)
                    save_progress(progress_data)
                    console.print("[italic]Lesson marked as completed![/italic]" if RICH_AVAILABLE else "Lesson marked as completed!")
                success = True
                sleep(1)
            else:
                console.print("[bold red]Incorrect Output.[/bold red]" if RICH_AVAILABLE else "Incorrect Output.")
                exp_title = "Expected Output"
                exp_content = normalized_expected.strip() # Display stripped version
                act_title = "Your Output"
                act_content = actual_stdout_raw if actual_stdout_raw.strip() else "[No Output]" # Show raw output

                if RICH_AVAILABLE:
                    console.print(Panel(exp_content, style="yellow", border_style="yellow", title=exp_title))
                    console.print(Panel(act_content, style="blue", border_style="blue", title=act_title))
                else:
                    console.print(f"--- {exp_title} ---\n{exp_content}\n-----------------")
                    console.print(f"--- {act_title} ---\n{act_content}\n---------------")
                # Hint: Maybe show a diff here in the future?
                sleep(1)

        except subprocess.TimeoutExpired:
            console.print("[bold red]Error: Your code took too long to execute (Timeout).[/bold red]" if RICH_AVAILABLE else "Error: Your code took too long to execute (Timeout).")
            console.print("[dim]Check for infinite loops or very long operations.[/dim]" if RICH_AVAILABLE else "Check for infinite loops or very long operations.")
        except FileNotFoundError:
             python_exe = sys.executable or 'python'
             console.print(f"[bold red]Error: Could not find Python interpreter ('{python_exe}'). Is it in your PATH?[/bold red]" if RICH_AVAILABLE else f"Error: Could not find Python interpreter ('{python_exe}'). Is it in your PATH?")
             sleep(3)
             return False # Indicate failure to run
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred during verification:[/bold red] {e}" if RICH_AVAILABLE else f"An unexpected error occurred during verification: {e}")
        finally:
             # Ensure continue prompt appears even on error
             try:
                 Prompt.ask("\n[cyan]Press Enter to continue...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to continue...")
             except Exception:
                 input("\nPress Enter to continue...")


    # --- Unknown Lesson Type ---
    else:
        console.print(f"[yellow]Warning: Unknown lesson type '{lesson_type}' for lesson '{lesson_id}'[/yellow]" if RICH_AVAILABLE else f"Warning: Unknown lesson type '{lesson_type}' for lesson '{lesson_id}'")
        sleep(2)

    return True # Indicate lesson was run successfully (or at least attempted)

# --- Main Application Loop (mostly unchanged, added better error handling) ---
def main():
    progress_data = load_progress()
    display_welcome()

    while True:
        clear_screen()
        try:
            choice = display_main_menu(progress_data)
            if choice is None: # Handle invalid input from menu
                 continue

            if choice == 1: # Start/Continue Learning
                while True: # Module Selection Loop
                    selected_module = display_module_selection(progress_data)
                    if selected_module is None:
                        break # Back to main menu

                    while True: # Lesson Selection Loop
                        selected_lesson = display_lesson_selection(selected_module, progress_data)
                        if selected_lesson is None:
                             break # Back to module selection

                        # Pass the whole progress_data dict
                        if not run_lesson(selected_lesson, progress_data):
                             # run_lesson returned False, maybe due to critical error
                             console.print("[bold red]Failed to run lesson due to a critical error. Returning to module selection.[/bold red]" if RICH_AVAILABLE else "Failed to run lesson due to a critical error. Returning to module selection.")
                             sleep(2.5)
                             break # Break lesson loop, go back to module select

            elif choice == 2: # View Progress
                clear_screen()
                if RICH_AVAILABLE:
                    console.print(Panel("[bold blue]Your Progress[/bold blue]", border_style="blue"))
                else:
                    console.print("\n--- Your Progress ---\n")

                completed_lessons = progress_data.get("completed_lessons", [])
                completed_count = len(completed_lessons)
                total_lessons = 0
                for module in LESSON_CONTENT:
                    total_lessons += len(module.get('lessons', []))

                if total_lessons > 0:
                     percentage = (completed_count / total_lessons) * 100 if total_lessons > 0 else 0
                     console.print(f"You have completed {completed_count} out of {total_lessons} lessons ({percentage:.1f}%).")
                     # Add more detail? List completed lesson IDs?
                     # console.print("\nCompleted Lesson IDs:")
                     # if completed_lessons:
                     #      console.print(", ".join(completed_lessons))
                     # else:
                     #      console.print("[dim]None yet.[/dim]")
                else:
                     console.print("No lessons available yet.")


                try: Prompt.ask("\n[cyan]Press Enter to return to the Main Menu...[/cyan]" if RICH_AVAILABLE else "\nPress Enter to return to the Main Menu...")
                except Exception: input("\nPress Enter to return to the Main Menu...")


            elif choice == 3: # Reset Progress
                 clear_screen()
                 console.print("[bold red]Reset Progress[/bold red]" if RICH_AVAILABLE else "Reset Progress")
                 try:
                      # Use Confirm for y/n prompt
                      if Confirm.ask("[yellow]Are you sure you want to reset all progress? This cannot be undone.[/yellow]" if RICH_AVAILABLE else "Are you sure you want to reset all progress? This cannot be undone. (y/n)", default=False):
                           progress_data = {"completed_lessons": []}
                           save_progress(progress_data)
                           console.print("[green]Progress has been reset.[/green]" if RICH_AVAILABLE else "Progress has been reset.")
                      else:
                           console.print("[dim]Progress reset cancelled.[/dim]" if RICH_AVAILABLE else "Progress reset cancelled.")
                 except Exception as e:
                      # Handle potential errors if Confirm fails (e.g., non-rich env issues)
                      console.print(f"[red]Could not process confirmation: {e}. Progress not reset.[/red]")
                 sleep(2)


            elif choice == 4: # Exit
                console.print("\n[bold cyan]Happy Coding! Goodbye![/bold cyan]" if RICH_AVAILABLE else "\nHappy Coding! Goodbye!")
                sys.exit(0)

            # Removed else clause as IntPrompt handles invalid choices now

        except (ValueError, TypeError) as e:
             # Catch errors from IntPrompt if conversion fails (though choices should prevent this)
             # Or other potential type errors in the loop
             console.print(f"\n[bold red]Invalid input or data error:[/bold red] {e}. Please try again." if RICH_AVAILABLE else f"\nInvalid input or data error: {e}. Please try again.")
             sleep(2)
        except KeyboardInterrupt:
             console.print("\n\n[bold yellow]Operation cancelled by user. Exiting.[/bold yellow]" if RICH_AVAILABLE else "\n\nOperation cancelled by user. Exiting.")
             sys.exit(1)
        except Exception as e:
             # General catch-all for unexpected issues in the main loop
             console.print(f"\n[bold red]An unexpected error occurred in the main loop:[/bold red] {e}" if RICH_AVAILABLE else f"\nAn unexpected error occurred in the main loop: {e}")
             # Optionally print traceback for debugging
             # import traceback
             # traceback.print_exc()
             console.print("[dim]Please report this error if it persists.[/dim]" if RICH_AVAILABLE else "Please report this error if it persists.")
             sleep(4)


if __name__ == "__main__":
    if not RICH_AVAILABLE:
        print("------------------------------------------------------")
        print("Warning: 'rich' library not found.")
        print("Falling back to basic terminal output.")
        print("For a better experience, please install it:")
        print("  pip install rich")
        print("------------------------------------------------------")
        sleep(3) # Give user time to read the warning
    main()