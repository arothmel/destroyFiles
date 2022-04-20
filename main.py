from pathlib import Path

root_dir = Path('destination')
# Create files
# for i in range(10, 21):
#     filename = str(i) + '.csv'
#     filepath = root_dir / Path(filename)
#     filepath.touch()

# destroy files - rewrite content before delete
# root_dir = Path('destination')
for path in root_dir.glob("*.csv"):
    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()
