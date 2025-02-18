from enum import Enum

from models.baseline_fill_mask_model import FillMaskModel
from models.baseline_generation_model import GenerationModel
from models.baseline_llama_3_chat_model import Llama3ChatModel
from models.rag_fill_mask_model import FillMaskModelRAG
from models.rag_generation_model import GenerationModelRAG
from models.rag_llama_3_chat_model import Llama3ChatModelRAG
from models._rag_fancy_fill_mask_model import FillMaskModelRAGfancy
from models._rag_fancy_generation_model import GenerationModelRAGfancy
from models._rag_fancy_llama_3_chat_model import Llama3ChatModelRAGfancy

from models.finetune_rag_fancy_llama_3_chat_model import Llama3ChatModelRAGFancyFinetuned


class Models(Enum):
    BASELINE_FILL_MASK = "baseline_fill_mask"
    BASELINE_GENERATION = "baseline_generation"
    BASELINE_LLAMA_3_CHAT = "baseline_llama_3_chat"
    RAG_FILL_MASK = "rag_fill_mask"
    RAG_GENERATION = "rag_generation"
    RAG_LLAMA_3_CHAT = "rag_llama_3_chat"
    RAG_FANCY_FILL_MASK = "rag_fancy_fill_mask"
    RAG_FANCY_GENERATION = "rag_fancy_generation"
    RAG_FANCY_LLAMA_3_CHAT = "rag_fancy_llama_3_chat"
    RAG_FANCY_LLAMA_3_CHAT_FINETUNED = "rag_fancy_llama_3_chat_finetuned"


    # Add more models here

    @staticmethod
    def get_model(model_name: str):
        model = Models(model_name)
        if model == Models.BASELINE_FILL_MASK:
            return FillMaskModel
        elif model == Models.RAG_FILL_MASK:
            return FillMaskModelRAG
        elif model == Models.BASELINE_GENERATION:
            return GenerationModel
        elif model == Models.BASELINE_LLAMA_3_CHAT:
            return Llama3ChatModel
        elif model==Models.RAG_GENERATION:
            return GenerationModelRAG
        elif model==Models.RAG_LLAMA_3_CHAT:
            return Llama3ChatModelRAG
        elif model==Models.RAG_FANCY_FILL_MASK:
            return FillMaskModelRAGfancy
        elif model==Models.RAG_FANCY_GENERATION:
            return GenerationModelRAGfancy
        elif model==Models.RAG_FANCY_LLAMA_3_CHAT:
            return Llama3ChatModelRAGfancy
        elif model==Models.RAG_FANCY_LLAMA_3_CHAT_FINETUNED:
            return Llama3ChatModelRAGFancyFinetuned
    
        else:
            raise ValueError(f"Model `{model_name}` not found.")
