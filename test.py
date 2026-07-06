import yaml
import ruamel.yaml

def get_tag_from_yaml_file(file_path):
    try:
        # Read the content of the YAML file
        with open(file_path, 'r') as file:
            yaml_content = file.read()

        # Split the YAML content into lines
        lines = yaml_content.split('\n')

        # Initialize variables to track the current context
        in_image_section = False
        tag_value = None

        # Iterate through the lines
        for line in lines:
            # Check if the line indicates the start of the 'image' section
            if line.strip() == 'image:':
                in_image_section = True
            elif in_image_section and line.startswith('  tag:'):
                # Extract the tag value
                tag_value = line.split(':')[-1].strip()
                break

        return tag_value

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        return None



def edit_yaml_tag(file_path, new_tag):
    try:
        # Load YAML content from the file
        yaml = ruamel.yaml.YAML()
        with open(file_path, 'r') as file:
            data = yaml.load(file)

        # Modify the 'tag' key
        if 'image' in data and 'tag' in data['image']:
            data['image']['tag'] = new_tag
            print(f"Tag in 'image' updated to '{new_tag}'.")

            # Dump the modified data back to the YAML file
            with open(file_path, 'w') as file:
                yaml.dump(data, file)
                print(f"Changes written to {file_path}.")
        else:
            print("Either 'image' or 'tag' key not found in the YAML file.")

    except ruamel.yaml.YAMLError as e:
        print(f"Error editing YAML file: {e}")



# Example usage:
source_yaml_file = '/Users/sarthaksatish/Desktop/Sarthak/GitHubProjects/helm-charts-2/manifests/employeemanagement/sit/immutable/values.yaml'
target_yaml_file = '/Users/sarthaksatish/Desktop/Sarthak/GitHubProjects/helm-charts-2/manifests/employeemanagement/pre/immutable/values.yaml'

# Extract image tag from the source file
# Example usage with file path:
tag_value = get_tag_from_yaml_file(source_yaml_file)

if tag_value is not None:
    print(f"The value of 'tag' is: {tag_value}")
else:
    print("Tag not found or there was an error.")




edit_yaml_tag(target_yaml_file, tag_value)
