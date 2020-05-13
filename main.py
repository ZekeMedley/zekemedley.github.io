import argparse
import pathlib
from zekedoc.zekedoc import render_file
from distutils.dir_util import copy_tree

def get_all_files(dirpath):
    assert(dirpath.is_dir())
    file_list = []
    for x in dirpath.iterdir():
        if x.is_file():
            file_list.append(x)
        elif x.is_dir():
            file_list.extend(get_all_files(x))
    return file_list

parser = argparse.ArgumentParser()
parser.add_argument('-md', dest='markdown_dir', type=str, required=True,
                    help='directory that markdown files are located in')
parser.add_argument('-od', dest='output_dir', type=str, required=True,
                    help='directory that html files will be generated in')

results = parser.parse_args()
# Create the output directory if it doesn't exist.
pathlib.Path(results.output_dir).mkdir(parents=True, exist_ok=True)

p = pathlib.Path(results.markdown_dir)
assert p.exists() and p.is_dir(), "Markdown directory does not exist."

files = get_all_files(p)

for path in files:
    with path.open() as f:
        output = render_file(f)

    # path is in the form markdown_dir/whatever
    # output needs to be in the form output_dir/whatever
    output_path = results.output_dir / path.relative_to(*p.parts[:2])
    
    # make the directory if it doesnt exist
    pathlib.Path(output_path.parents[0]).mkdir(parents=True, exist_ok=True)
    output_path.write_text(output)
    output_path.rename(output_path.with_suffix('.md.html'))
    
    # copy over styles into new dir
    copy_tree("styles", results.output_dir + "/styles")
    copy_tree("media", results.output_dir + "/media")
    copy_tree("js", results.output_dir + "/js")
    copy_tree("static", results.output_dir + "/static")
