"""
InWork-Ai: Shared-Schema Database Strategy
File: database.py
Purpose: Demonstrates the 'Flat Columns' strategy for a Multi-Tenant B2B SaaS.
Implementation: Using SQLAlchemy 2.0.
"""

from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Interaction(Base):
    """
    Main Interaction table using a 'Flat' strategy to avoid 
    expensive joins across 60+ business parameters.
    """
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, index=True, nullable=False)
    
    # Core Interaction Data
    session_id = Column(String(50), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Flat Columns for SSOT (Single Source of Truth)
    # These are filled by the Analytical Agent (GLM-4) after the call
    customer_name = Column(String(100))
    customer_phone = Column(String(20))
    intent_category = Column(String(50))
    sentiment_score = Column(Integer)  # 1-10
    
    # Deep Context Data (MiMo 1M Window Target)
    # Stores raw transcript and business-specific attributes
    raw_transcript = Column(String)
    extracted_features = Column(JSON) 
    
    # Business Logic State
    next_step = Column(String(100))
    is_compliant = Column(Integer, default=1)

# --- Design Rationale ---
# 1. Shared Schema: All tenants share one table (filtered by RLS).
# 2. Performance: Flat columns allow for sub-ms reporting and dashboarding.
# 3. Scalability: Ready for millions of records across thousands of B2B tenants.
