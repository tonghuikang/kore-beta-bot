# produces warnings which can be ignored, but I hope to resolve this
# upload the notebook_generated.ipynb onto Kaggle and "Save & Run All"

import nbformat
import nbformat.v4 as nbf





cells = []

preamble_intro = """
# [Kore 2022] Kore Beta Bot
I have not worked on this. See
- https://github.com/w9PcJLyb/kore-beta-bot
- https://www.kaggle.com/competitions/kore-2022-beta/discussion/317737
"""
cells.append(nbf.new_markdown_cell(preamble_intro))


init_code = """\
!pip install --user kaggle-environments > /dev/null\
"""
cells.append(nbf.new_code_cell(init_code, metadata={"_kg_hide-input": True}))





preamble_agent = """\
# Files Upload\
"""
cells.append(nbf.new_markdown_cell(preamble_agent))


filenames = [
    "basic.py",
    "board.py",
    "control.py",
    "defence.py",
    "expantion.py",
    "geometry.py",
    "helpers.py",
    "logger.py",
    "main.py",
    "mining.py",
    "offence.py",
]

for filename in filenames:
    savefile_cell_magic = f"%%writefile {filename}\n"
    with open("src/" + filename, "r") as f:
        content = savefile_cell_magic + f.read()
    cell = nbf.new_code_cell(content, metadata={"_kg_hide-input": True})
    cells.append(cell)





preamble_rendering = """\
# Game Rendering
This is a replay of the agent fighting against the baseline bot.\
"""
cells.append(nbf.new_markdown_cell(preamble_rendering))


runner_code = """\
from kaggle_environments import make
env = make("kore_fleets", debug=True)
print(env.name, env.version)\
"""
cells.append(nbf.new_code_cell(runner_code, metadata={"_kg_hide-input": True}))


runner_code = """\
from kaggle_environments.envs.kore_fleets.starter_bots.python.main import agent
env.run([agent, "/kaggle/working/main.py"])
env.render(mode="ipython", width=900, height=800)\
"""
cells.append(nbf.new_code_cell(runner_code, metadata={"_kg_hide-input": True, "jupyter": {"outputs_hidden":True}}))





preamble_evaluation = """\
# Evaluation
Run multiple matches for winrate.
To be added.\
"""
cells.append(nbf.new_markdown_cell(preamble_evaluation))





preamble_debugging = """\
# Debugging
See board state.
To be added.\
"""
cells.append(nbf.new_markdown_cell(preamble_evaluation))





preamble_submission = """\
# Submission
Make a tar.gz archive for submission.\
"""
cells.append(nbf.new_markdown_cell(preamble_submission))


zip_code = """\
!rm -rf __pycache__/
!tar --exclude='*.ipynb' --exclude="*.pyc" -czf submission.tar.gz *\
"""

cells.append(nbf.new_code_cell(zip_code, metadata={"_kg_hide-input": True}))





notebook_metadata = {
    "kernelspec": {
        "language": "python",
        "display_name": "Python 3",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.7.10",
        "mimetype": "text/x-python",
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "pygments_lexer": "ipython3",
        "nbconvert_exporter": "python",
        "file_extension": ".py"
    }
}

nb = nbf.new_notebook(cells=nbformat.from_dict(cells), metadata=notebook_metadata)

with open('kore-beta-bot.ipynb', 'w') as f:
    nbformat.write(nb, f)
