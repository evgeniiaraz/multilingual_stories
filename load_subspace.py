import argparse
import os

STORY_IDS = [1, 110, 111, 141, 156, 158, 201, 210, 234, 243, 262, 27, 291, 294, 296, 30, 315, 324, 327, 337, 342, 4, 52, 6, 66, 72, 89, 95]


parser = argparse.ArgumentParser()
parser.add_argument('--language', type=str, help="Language code")
args = parser.parse_args()

print(args.language)

lang_dir = os.path.join("global-asp", args.language)
for filename in os.listdir(lang_dir):
	if "README" in filename or int(filename.split("_")[0]) not in STORY_IDS:
		os.remove(os.path.join(lang_dir, filename))