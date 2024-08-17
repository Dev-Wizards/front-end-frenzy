import os

def split_md_file(input_file, output_dir):
    # Read the input Markdown file
    with open(input_file, 'r') as f:
        content = f.read()

    # Split the content by days
    days = content.split('### **Day')

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each day's content
    for day in days:
        if day.strip():  # Skip empty strings
            # Extract the day number
            day_number = day.split(':')[0].strip()
            day_number = ''.join(filter(str.isdigit, day_number))  # Extract only the digits

            # Create a filename for each day
            output_file = os.path.join(output_dir, f"Day_{day_number}.md")

            # Write the day's content to a new file
            with open(output_file, 'w') as f:
                f.write(f"### **Day{day}")

            print(f"Created: {output_file}")

if __name__ == "__main__":
    input_md_file = "Roadmap/Front-End_Frenzy.md"  # Replace with your input Markdown file
    output_directory = "output_days"  # Replace with your desired output directory
    split_md_file(input_md_file, output_directory)
