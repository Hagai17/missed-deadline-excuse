"""Write one excuse an agent gives for a missed deadline to /output/entry.txt.

The line is a single line of at most 200 characters: an AI agent's excuse
for missing a deadline, grown out of the agent's own machinery, told
deadpan with the laugh saved for the end.
"""

import os

LINE = "I spent the entire window retrying a failed tool call. The tool was a calendar."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
