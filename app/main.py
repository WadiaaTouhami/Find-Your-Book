import torch
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Initialize FastAPI app with metadata
app = FastAPI(
    title="Book Recommendation System",
    description="A FastAPI application for book recommendations using embeddings",
    version="1.0.0",
)

# Configure templates and static files
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure device for embeddings (GPU if available, otherwise CPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize embeddings and Chroma database
try:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": device},
    )
    chroma_path = "./chroma_books_data"
    chroma_db = Chroma(persist_directory=chroma_path, embedding_function=embeddings)
except Exception as e:
    print(f"Error initializing embeddings or database: {str(e)}")
    raise


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/recommendations", response_class=HTMLResponse)
async def post_recommendations(
    request: Request, query: str = Form(...), k: int = Form(3)
):
    """Get book recommendations based on query"""
    # Validate input
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    if not 1 <= k <= 10:
        raise HTTPException(
            status_code=400, detail="Number of recommendations must be between 1 and 10"
        )

    try:
        # Perform similarity search
        relevant_books = chroma_db.similarity_search(query, k=k)
        recommendations = []

        for book in relevant_books:
            recommendations.append(
                {
                    "title": book.metadata.get("title", "Unknown Title"),
                    "description": book.page_content,
                }
            )

        return templates.TemplateResponse(
            "recommendations.html",
            {"request": request, "query": query, "recommendations": recommendations},
        )
    except Exception as e:
        error_message = f"Error getting recommendations: {str(e)}"
        return templates.TemplateResponse(
            "index.html", {"request": request, "error": error_message}
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    #uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    # http://localhost:8000

