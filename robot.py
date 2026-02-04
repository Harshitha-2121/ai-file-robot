from ai_brain import interpret_command
from file_ops import find_all_pdfs, move_pdfs

print("🤖 AI File Robot is READY")
print("Type 'exit' to quit\n")

while True:
    command = input(">>> ")

    if command.lower() == "exit":
        break

    try:
        action = interpret_command(command)

        if action["action"] == "find_pdfs":
            pdfs = find_all_pdfs()
            print(f"✅ Found {len(pdfs)} PDFs")

        elif action["action"] == "move_pdfs":
            folder = action.get("folder", "All_PDFs")
            msg = move_pdfs(folder)
            print("✅", msg)

        else:
            print("❌ Unknown action")
            

    except Exception as e:
        print("⚠ Error:", e)
