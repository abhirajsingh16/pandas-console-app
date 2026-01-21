import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("leads.csv", index_col=False)

a = True
fields = [
    "Account Id",
    "Lead Owner",
    "First Name",
    "Last Name",
    "Company",
    "Phone 1",
    "Phone 2",
    "Email 1",
    "Email 2",
    "Website",
    "Source",
    "Deal Stage",
    "Notes",
]


while a:
    print(
        "Enter\n1. Append values\n2. Remove values\n3. Display\n4. Pie Chart\n5. Bar Graph\n6. Exit"
    )
    a = int(input(":"))

    match a:

        case 1:
            row = []
            for field in fields:

                value = input(f"Enter {field}: ")

                if field == "Account Id" and value in df["Account Id"].values:
                    print("Enter valid account ID (already exists)")
                    break

                if value == "":
                    value = None
                row.append(value)

            if len(row) == len(fields):

                new_row = pd.DataFrame([row], columns=fields)

                df = pd.concat([df, new_row], ignore_index=True)

                df.to_csv("leads.csv", index=False)

                print("\n Row appended successfully!\n")

        case 2:
            acc_id = input("Enter account ID to remove:")
            if acc_id in df["Account Id"].values:
                df = df[df["Account Id"] != acc_id]
                df.to_csv("leads.csv", index=False)
                print(f"{acc_id} account has been removed")
            else:
                print("Invalid account ID:\n")

        case 3:
            try:
                i = eval(input("Enter values to output index (start, stop):"))
                if type(i) == tuple and len(i) == 2 and i[0] < i[1]:
                    print(df.iloc[i[0] : (i[1] + 1)])
                    print()
                else:
                    print(
                        "Enter values properly please. two numbers seperated by commas\n"
                    )
            except:
                print("Enter values properly please. two numbers seperated by commas\n")

        case 4:
            df["Source"].value_counts().plot(kind="pie")
            plt.show()
            print()
        case 5:
            s = df.Source.value_counts().head(100)
            s.plot(kind="bar", color="green", figsize=(15, 5))
            plt.ylabel("Frequency")
            plt.title("Best sources")
            plt.xticks(rotation=45, ha="right")
            plt.show()
            print()

        case 6:
            a = False
