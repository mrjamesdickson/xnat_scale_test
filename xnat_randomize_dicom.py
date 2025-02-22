import pydicom
import random
import os
import argparse

# Function to generate random numeric string of a given length
def generate_random_numeric_string(length=12):
    return ''.join(random.choices('0123456789', k=length))

# Function to ensure that the UID does not exceed 64 characters
def append_to_uid(existing_uid, random_length=8):
    # Calculate the maximum length of the random string that can be appended
    max_random_length = 64 - len(existing_uid)
    
    # Ensure the random string doesn't exceed the maximum allowed length
    random_string = generate_random_numeric_string(min(random_length, max_random_length))
    
    return existing_uid + random_string

# Function to modify DICOM fields with random values
def modify_dicom(dicom_file, output_dir, project, num_iterations=100000):
    # Load the original DICOM file
    original_dicom = pydicom.dcmread(dicom_file)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_iterations):
        # Create a copy of the original DICOM object
        dicom_copy = original_dicom.copy()

        # Randomize PatientID and PatientName
        dicom_copy.PatientID = generate_random_numeric_string(12)
        dicom_copy.PatientName = generate_random_numeric_string(10)

        # Append a random numeric string to the existing UID fields, ensuring they don't exceed 64 characters
        if 'SOPInstanceUID' in dicom_copy:
            dicom_copy.SOPInstanceUID = append_to_uid(dicom_copy.SOPInstanceUID)
        if 'StudyInstanceUID' in dicom_copy:
            dicom_copy.StudyInstanceUID = append_to_uid(dicom_copy.StudyInstanceUID)
        if 'SeriesInstanceUID' in dicom_copy:
            dicom_copy.SeriesInstanceUID = append_to_uid(dicom_copy.SeriesInstanceUID)

        # Populate the PatientComments field with the specified format
        dicom_copy.PatientComments = f"Project:{project} Subject:{dicom_copy.PatientName} Session:{dicom_copy.PatientID}"

        # Construct the output filename
        output_filename = f"{i+1:05d}_modified.dcm"  # Naming the file with a counter (e.g., 00001_modified.dcm)

        # Save the modified DICOM file
        if not os.path.exists(os.path.join(output_dir, output_filename)):
            dicom_copy.save_as(os.path.join(output_dir, output_filename))

            # Print the description of the saved file
            print(f"Saving file {output_filename} with PatientName: {dicom_copy.PatientName}, "f"PatientID: {dicom_copy.PatientID}, PatientComments: {dicom_copy.PatientComments}")
        else:
             print(f"Skipping file {output_filename} with PatientName: {dicom_copy.PatientName}, "f"PatientID: {dicom_copy.PatientID}, PatientComments: {dicom_copy.PatientComments}")
        # Optionally print progress every 10,000 files
        if (i + 1) % 10000 == 0:
            print(f"Processed {i + 1} files")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Modify DICOM files with random numeric values")
    parser.add_argument("dicom_file", type=str, help="Path to the original DICOM file")
    parser.add_argument("output_dir", type=str, help="Directory to save modified DICOM files")
    parser.add_argument("project", type=str, help="Project name to populate PatientComments")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to modify the DICOM files
    modify_dicom(args.dicom_file, args.output_dir, args.project)
    print("Completed DICOM modifications.")

if __name__ == "__main__":
    main()
