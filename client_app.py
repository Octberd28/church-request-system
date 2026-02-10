import requests

REQ_URL = "http://localhost:5001/requests"
LOG_URL = "http://localhost:5002/log"


departments = [
    "Elders Corp",
    "Deacon Department",
    "Deaconess Department",
    "Sabbath School",
    "Missionary Work",
    "Youth Society",
    "Women Department"
]


def pause():
    input("\nPress Enter to continue...")


def choose_department():
    print("\nSelect Department:")
    for i, d in enumerate(departments, 1):
        print(f"{i}. {d}")

    try:
        choice = int(input("Choice: "))
        return departments[choice - 1]
    except:
        print("Invalid selection.")
        return None


def submit_request():
    dept = choose_department()
    if not dept:
        return

    print(f"\nDepartment selected: {dept}")

    desc = input("Enter request description:\n> ")

    data = {
        "department": dept,
        "description": desc
    }

    requests.post(REQ_URL, json=data)
    requests.post(LOG_URL,
                  json={"message": f"Request submitted by {dept}"})

    print("\nRequest submitted successfully!")
    pause()


def view_requests():
    r = requests.get(REQ_URL).json()

    if not r:
        print("\nNo requests found.")
    else:
        print("\n--- REQUEST LIST ---")
        for i, req in enumerate(r):
            print(f"\nRequest #{i}")
            print(f"Department: {req['department']}")
            print(f"Description: {req['description']}")
            print(f"Status: {req['status']}")

    pause()


def approve_request():
    r = requests.get(REQ_URL).json()

    if not r:
        print("No requests available.")
        pause()
        return

    view_requests()

    try:
        idx = int(input("\nSelect request #: "))
        if idx < 0 or idx >= len(r):
            raise ValueError
    except:
        print("Invalid selection.")
        return

    decision = input("Approve or Reject? ").capitalize()

    if decision not in ["Approve", "Reject"]:
        print("Invalid decision.")
        return

    requests.put(
        f"{REQ_URL}/{idx}",
        json={"status": decision}
    )

    requests.post(LOG_URL,
                  json={"message": f"Request {idx} {decision}"})

    print("Decision recorded.")
    pause()


while True:
    print("\n--- MAIN MENU ---")
    print("1 Submit Request")
    print("2 View Requests")
    print("3 Approve/Reject")
    print("4 Exit")

    choice = input("> ")

    if choice == "1":
        submit_request()
    elif choice == "2":
        view_requests()
    elif choice == "3":
        approve_request()
    elif choice == "4":
        break
    else:
        print("Invalid option.")
