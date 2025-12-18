# FinanceScope

## Overview

FinanceScope is an intelligent document analysis system that transforms unstructured financial and legal PDFs into actionable insights through natural language processing and interactive visualizations. The platform combines RAG (Retrieval-Augmented Generation) technology with automated data extraction to enable rapid analysis of complex financial documents.

## Problem Statement

Financial analysts, legal professionals, and investment teams spend considerable time manually reviewing lengthy reports, extracting key metrics, and creating comparative analyses. This process is time-consuming, error-prone, and scales poorly across multiple documents.

FinanceScope addresses these challenges by:
- Automating data extraction from PDF documents
- Enabling natural language queries against document content
- Generating structured datasets from unstructured sources
- Providing interactive dashboards for comparative analysis
- Maintaining source traceability through precise citations

## Core Features

### Intelligent Document Processing
- Multi-document upload and batch processing
- Advanced PDF parsing with table and numerical data extraction
- Context-aware chunking strategies for optimal retrieval
- Metadata preservation for source tracking

### Natural Language Query Interface
- Conversational question-answering system
- Response generation with page-level citations
- Support for comparative queries across multiple documents
- Context-aware follow-up question handling

### Automated Data Extraction
- LLM-powered identification of financial metrics
- Structured data generation from narrative text
- Validation and normalization of extracted values
- Export capabilities in JSON and CSV formats

### Interactive Dashboard
- Dynamic visualization of extracted financial data
- Time-series analysis and trend identification
- Multi-document comparison capabilities
- Customizable metric selection and filtering
- Export-ready charts and reports

## Technical Architecture

### Technology Stack

**Core Framework:**
- Python 3.10+
- LangChain for RAG orchestration
- OpenAI GPT-4 for analysis and extraction
- OpenAI text-embedding-3-small for vectorization

**Data Layer:**
- ChromaDB for vector storage
- Pandas for data manipulation
- Pydantic for data validation

**Interface:**
- Streamlit for web interface
- Plotly for interactive visualizations
- FastAPI for REST endpoints (optional)

**Document Processing:**
- PyPDF2 for PDF parsing
- pdfplumber for table extraction
- Unstructured for complex layout handling

### System Components
```
┌─────────────────┐
│  PDF Documents  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Extraction    │◄─── LLM-powered parsing
│   & Chunking    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Vector Storage  │◄─── Embeddings + Metadata
│   (ChromaDB)    │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌──────────────┐
│  Q&A   │ │ Data Extract │
│ Engine │ │  & Dashboard │
└────────┘ └──────────────┘
```

### Processing Pipeline

1. **Document Ingestion:** PDF upload and validation
2. **Text Extraction:** Parse document structure and content
3. **Chunking:** Intelligent segmentation with overlap
4. **Vectorization:** Generate embeddings for semantic search
5. **Storage:** Persist vectors with metadata in ChromaDB
6. **Retrieval:** Similarity search based on user queries
7. **Generation:** LLM-powered response with citations
8. **Extraction:** Structured data identification and validation
9. **Visualization:** Interactive dashboard generation

## Installation

### Prerequisites

- Python 3.10 or higher
- OpenAI API key
- 4GB RAM minimum (8GB recommended)
- 2GB disk space for dependencies and vector storage

### Setup
```bash
# Clone the repository
git clone https://github.com/PedroJuanOfc/finance-scope.git
cd finance-scope

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### Environment Variables
```
OPENAI_API_KEY=your_api_key_here
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
VECTOR_DB_PATH=./chroma_db
```

## Usage

### Starting the Application
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Basic Workflow

1. **Upload Documents:** Select one or more PDF files containing financial reports
2. **Process Documents:** System automatically extracts and indexes content
3. **Ask Questions:** Use natural language to query document content
4. **Extract Data:** Select metrics to extract into structured format
5. **Generate Dashboard:** Visualize extracted data with interactive charts
6. **Export Results:** Download data tables or chart images

### Example Queries
```
- "What was the net revenue for Q3 2024?"
- "Compare operating expenses across all quarters"
- "List all regulatory compliance mentions"
- "What are the main risk factors identified?"
- "Show the trend in profit margins over the fiscal year"
```

## Project Structure
```
finance-scope/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── README.md                  # This file
├── src/
│   ├── __init__.py
│   ├── document_processor.py  # PDF parsing and chunking
│   ├── vectorstore.py         # ChromaDB management
│   ├── rag_engine.py          # Query and retrieval logic
│   ├── data_extractor.py      # Structured data extraction
│   ├── dashboard.py           # Visualization components
│   └── utils.py               # Helper functions
├── tests/
│   ├── test_processor.py
│   ├── test_rag.py
│   └── test_extractor.py
├── data/
│   ├── sample_reports/        # Example PDF files
│   └── extracted/             # Exported data files
└── docs/
    ├── architecture.md        # Detailed architecture
    ├── api_reference.md       # API documentation
    └── development.md         # Development guide
```

## Development

### Running Tests
```bash
pytest tests/ -v
```

### Code Quality
```bash
# Format code
black src/

# Lint
flake8 src/

# Type checking
mypy src/
```

### Adding New Features

1. Create feature branch from `main`
2. Implement changes with tests
3. Update documentation
4. Submit pull request

## Performance Considerations

### Optimization Strategies

- **Chunking:** Tested configurations for optimal retrieval (size: 1000, overlap: 200)
- **Embedding Model:** Using text-embedding-3-small for cost-efficiency
- **LLM Selection:** GPT-4o-mini provides strong performance at lower cost
- **Caching:** Vector storage persists between sessions
- **Batch Processing:** Parallel document processing for multiple files

### Benchmarks

- Single document processing: 10-30 seconds (depending on length)
- Query response time: 2-5 seconds
- Data extraction: 15-45 seconds per document
- Dashboard generation: 3-8 seconds

## Cost Analysis

Approximate costs per document (20-page financial report):

- Embedding generation: $0.002
- Query responses (10 queries): $0.015
- Data extraction: $0.008
- Total per document: ~$0.025

Monthly estimate for 100 documents: ~$2.50 in API costs

## Limitations and Future Work

### Current Limitations

- PDF-only support (no Word, Excel, or scanned documents)
- English language optimization (multilingual support planned)
- Single-user operation (no multi-tenancy)
- Local storage only (cloud integration planned)

### Roadmap

- [ ] Support for scanned documents via OCR
- [ ] Multi-language support
- [ ] Collaborative features and document sharing
- [ ] Advanced chart customization
- [ ] Automated report generation
- [ ] Integration with financial data APIs
- [ ] Fine-tuned models for domain-specific extraction
- [ ] Real-time document monitoring and alerts

## Contributing

Contributions are welcome. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Update documentation
6. Submit pull request with clear description

## License

MIT License - see LICENSE file for details

## Acknowledgments

- LangChain for RAG framework
- OpenAI for language models
- Streamlit for rapid UI development
- ChromaDB for vector storage solution

## Contact

**Pedro Juan Ferreira Saraiva**  
Brasília, Federal District, Brazil

- Email: pedrosaraivaofc@gmail.com
- LinkedIn: [Pedro Juan Ferreira Saraiva](https://www.linkedin.com/in/pedro-juan-ferreira-saraiva/)
- GitHub: [@PedroJuanOfc](https://github.com/PedroJuanOfc)

For questions, issues, or feature requests, please open an issue on the [GitHub repository](https://github.com/PedroJuanOfc/finance-scope/issues).

## Citation

If you use FinanceScope in your research or project, please cite:
```bibtex
@software{financescope2024,
  title={FinanceScope: Intelligent Financial Document Analysis},
  author={Saraiva, Pedro Juan Ferreira},
  year={2025},
  url={https://github.com/PedroJuanOfc/finance-scope}
}
```
