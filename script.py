
import subprocess
import os
import sys

# Paths to tools
XFS_TOOL = "./xfs_undelete"
BTRFS_SCRIPT = "./undelete.sh"

def run_xfs_tool():
    device = input("Enter the XFS device path (e.g. /dev/loop5): ").strip()
    if not os.path.exists(device):
        print(f"❌ Device {device} not found.")
        return
    if not os.path.isfile(XFS_TOOL):
        print("❌ XFS undelete tool not found!")
        return
    print(f"\n🧪 Running XFS undelete on {device}...\n")
    subprocess.run([XFS_TOOL, "-i", "", device])

def run_btrfs_tool():
    device = input("Enter the Btrfs device path (e.g. /dev/loop4): ").strip()
    output_dir = input("Enter the output recovery directory (e.g. ./btrfs_recov): ").strip()

    if not os.path.exists(device):
        print(f"❌ Device {device} not found.")
        return
    if not os.path.isfile(BTRFS_SCRIPT):
        print("❌ Btrfs undelete script not found!")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Created output directory: {output_dir}")

    print(f"\n🧪 Running Btrfs undelete on {device}, output to {output_dir}...\n")
    subprocess.run([BTRFS_SCRIPT, device, output_dir])

def main_menu():
    while True:
        print("\n=== Unified Filesystem Undelete Tool ===")
        print("1. Run XFS Undelete Tool")
        print("2. Run Btrfs Undelete Tool")
        print("3. Quit")
        choice = input("Enter your choice [1-3]: ").strip()

        if choice == "1":
            run_xfs_tool()
        elif choice == "2":
            run_btrfs_tool()
        elif choice == "3":
            print("👋 Exiting.")
            sys.exit(0)
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
