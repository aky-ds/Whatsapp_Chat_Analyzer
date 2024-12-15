# WhatsApp Chat Analyzer

This WhatsApp Chat Analyzer is a powerful tool built with Python that provides insights into WhatsApp chat data. The application reads a `.txt` file containing exported chat data and analyzes it to provide detailed statistics and visualizations. The tool identifies the most active users in a group, shows the most frequently used words, and presents these insights through interactive plots.

---

## Features

- **User Activity Analysis**: Identifies the most online users in a group.
- **Word Frequency Analysis**: Displays the most commonly used words in the chat.
- **Interactive Visualizations**: Generates plots for insights using Seaborn and Matplotlib.
- **Text File Support**: Accepts exported chat data in `.txt` format.
- **User-Friendly Interface**: Built using Streamlit for a clean and interactive UI.

---

## Tech Stack

- **Programming Language**: Python
- **Libraries Used**:
  - `streamlit` - For building the interactive interface.
  - `numpy` - For data manipulation and numerical operations.
  - `pandas` - For data analysis and preprocessing.
  - `seaborn` - For creating advanced visualizations.
  - `matplotlib` - For plotting.
  -   `nltk` - For natural language processing.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aky-ds/Whatsapp_Chat_Analyzer.git
   cd whatsapp-chat-analyzer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Export Chat Data**:
   - Export the WhatsApp chat as a `.txt` file (without including media).

2. **Upload the File**:
   - Use the Streamlit app to upload the exported `.txt` file.

3. **Analyze the Data**:
   - View detailed insights, including:
     - The most active users in the group.
     - A word cloud of the most commonly used words.
     - Bar charts and visualizations showing user activity trends.

---

## File Structure

```
whatsapp-chat-analyzer/
├── app.py                 # Main application script
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── sample_chat.txt        # Sample chat data
```

---

## Sample Visualizations

### 1. Most Active Users
Bar chart showing the users who are online most frequently in the group:

![Most Active Users](https://via.placeholder.com/600x400)

### 2. Word Cloud
A word cloud representing the most commonly used words in the chat

---

## Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For any inquiries or feedback, please contact ayazulhaqyousafzai(mailto:syedthescientist@example.com).
