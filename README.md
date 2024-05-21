# PennGPT

Penn State Harrisburg's Academic Chatbot!

Welcome to PennGPT, a powerful application that leverages OpenAI's GPT-4 and LangChain to provide insightful answers to your queries from a PDF document. This project uses Streamlit for the frontend interface, making it interactive and user-friendly.

## Features

- **Document Loading**: Efficiently load and process PDF documents.
- **Text Splitting**: Split the document into manageable chunks for better processing.
- **Vector Storage**: Use Chroma to store document vectors for efficient retrieval.
- **Embeddings**: Generate embeddings using OpenAI for document retrieval.
- **Query Answering**: Retrieve and generate answers to user queries based on the loaded document.
- **Streamlit Interface**: Provide a user-friendly web interface for interaction.

## GPT as an Academic Advisor

![UI1!](images/DeployedTest2.png)

## Installation

### Prerequisites

- Python 3.7+
- An OpenAI API key
- Streamlit
- LangChain
- PyMuPDF
- Chroma

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/PranitMaldikar/PennGPT.git
    cd PennGPT
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```env
    API_KEY=your_openai_api_key_here
    ```

5. **Prepare Your PDF Document**

    Place your PDF document (e.g., `edited_mergedData.pdf`) in the root directory.

6. **Run the Application**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Start the Application**

    Run the Streamlit app as described in the setup section.

2. **Upload PDF**

    Ensure your PDF is named `edited_mergedData.pdf` and is placed in the root directory.

3. **Query**

    Enter your query in the text input field and press Enter. The application will process your query and display the response based on the content of the PDF document.

## Intentionally Providing "Open-Ended" or "Ambiguous" Questions

![UI2!](images/DeployedTest1.png)

## Project Structure

- `app.py`: Main application file.
- `requirements.txt`: List of required Python packages.
- `storage/`: Directory for storing vector database.
- `edited_mergedData.pdf`: The PDF document to be processed.
- `logo.jpg`: Logo image displayed in the Streamlit interface.
- `.env`: Environment variables file.

## Dependencies

- `langchain`
- `streamlit`
- `pymupdf`
- `chromadb`
- `openai`
- `python-dotenv`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact Pranit Shrikrishna Maldikar at [pranitmaldikar@gmail.com](mailto:pranitmaldikar@gmail.com).
