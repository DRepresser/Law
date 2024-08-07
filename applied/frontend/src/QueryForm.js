import { useState } from 'react';
import axios from 'axios';
import { BounceLoader } from 'react-spinners';
import ReactMarkdown from 'react-markdown';

const api = axios.create({
    baseURL: 'http://localhost:8000'
})

const Expander = ({ title, content }) => {
    const [isOpen, setIsOpen] = useState(false);
    return (
        <div className="expander">
            <b onClick={() => setIsOpen(!isOpen)} className="expander-title">{title}</b>
            {isOpen && <p className="expander-content">{content}</p>}
        </div>
    );
};

function QueryForm() {
    const [query, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    const [documents, setDocuments] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const handleIndexing = async(e) => {
        e.preventDefault();
        setAnswer('');
        setIsLoading(true);
        const response = await api.post('/retrieve', { message: query });
        console.log(response)
        setAnswer(response.data.answer);
        setDocuments(response.data.documents)
        setIsLoading(false);
    }

    return (
        <div className="main-container">
            <form className="form">
                <input className="form-input" type="text" value={query} onChange={(e) => setQuestion(e.target.value)} />
                <div className="button-container">
                    <button className="form-button" type="submit" onClick={handleIndexing}>submit</button>
                </div>
            </form>
            {isLoading && (
                <div className="loader-container">
                    <BounceLoader color="#3498db" />
                </div>
            )}
            {answer && ( 
            <div className="results-container">
                <div className="results-answer">
                    <h2>Answer:</h2>
                    <ReactMarkdown>{answer}</ReactMarkdown>
                </div>
                <div className="results-documents">
                    <h2>Documents:</h2>
                    <ul>
                        {documents.map((documents, index) => (
                            <Expander key={index} title={documents.page_content.split(" ").slice(0, 5).join(" ") + "..."} content={documents}/>
                        ))}
                    </ul>
                </div>
            </div>
            )}
        </div>
        );
}

export default QueryForm;

