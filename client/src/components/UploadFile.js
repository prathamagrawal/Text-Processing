import { useState, useRef } from "react";
const UploadFile = () => {

    const [files, setFiles] = useState(null);
    const inputRef = useRef();

    const handleDragOver = (event) =>{
        event.preventDefault();
    }
    const handleDrop = (event) => {
        event.preventDefault();
        setFiles(event.dataTransfer.files);
    }

    const handleUpload = () => {};

    if(files) return (
        <div className="uploads">
            <ul>
                {Array.from(files).map((file,idx) => <li key={idx}>{file.name}</li>)}
            </ul>
            <div className="actions">
                <button onClick={() => setFiles(null)}>Cancel</button>
                <button onClick={handleUpload}>Upload</button>
            </div>
        </div>
    )

    return (
        <>{!files && (
            // <body>
                <div className="dragzone"
                    onDragOver={handleDragOver}
                    onDrop={handleDrop}                
                >
                    <h2>Drag and drop files to upload</h2>
                    <h2> or </h2>
                    <input type="file" 
                    onChange={(event) => setFiles(event.target.files)}
                    hidden 
                    ref={inputRef}
                    />
                    <button onClick={() => inputRef.current.click()}> Select files</button>
                </div>
            // </body>
        )}
        </>
    );
};

export default UploadFile;