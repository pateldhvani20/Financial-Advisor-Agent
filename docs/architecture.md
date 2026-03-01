# System Architecture – Week 1

## Phase 1 (Track A)

Streamlit Frontend
        ↓
OCR Module
        ↓
Expense Categorizer
        ↓
Financial Logic Engine
        ↓
Advice Engine (Rule-Based)

## Data Flow

1. User uploads screenshot or enters financial details.
2. OCR extracts transaction text.
3. Expense parser extracts amount and merchant.
4. Categorizer assigns expense category.
5. Financial logic engine calculates budgeting ratios.
6. Advice engine generates structured recommendations.

## Upgrade Path (Phase 2)

React → FastAPI → RAG Layer → LLM → Real-Time APIs