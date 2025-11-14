"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import date

# Example schemas (you can keep these for reference)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Logistics ERP schemas

StatusType = Literal[
    "draft", "pending", "in_transit", "delivered", "cancelled", "archived"
]

class Customer(BaseModel):
    """
    Customers of the logistics company
    Collection: "customer"
    """
    name: str = Field(..., description="Customer company or person name")
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    npwp: Optional[str] = Field(None, description="Tax ID (NPWP)")
    address: Optional[str] = Field(None, description="Primary address")
    city: Optional[str] = Field(None, description="City")
    country: str = Field("Indonesia", description="Country")
    notes: Optional[str] = Field(None, description="Internal notes")
    is_active: bool = Field(True, description="Active customer")

class Shipment(BaseModel):
    """
    Shipment orders for trucking/freight forwarding
    Collection: "shipment"
    """
    reference_no: str = Field(..., description="Internal reference number")
    customer_id: Optional[str] = Field(None, description="Linked customer ID")
    origin: str = Field(..., description="Origin location")
    destination: str = Field(..., description="Destination location")
    pickup_date: Optional[date] = Field(None, description="Pickup date")
    delivery_date: Optional[date] = Field(None, description="Delivery date")
    vehicle_type: Optional[str] = Field(None, description="Truck type (CDD, Fuso, Tronton)")
    status: StatusType = Field("pending", description="Shipment status")
    pieces: Optional[int] = Field(1, ge=0, description="Number of pieces")
    weight_kg: Optional[float] = Field(None, ge=0, description="Total weight in KG")
    volume_cbm: Optional[float] = Field(None, ge=0, description="Total volume in CBM")
    price_idr: Optional[float] = Field(None, ge=0, description="Total price in IDR")
    remarks: Optional[str] = Field(None, description="Additional notes")

class AuditLog(BaseModel):
    """
    Simple audit trail entries
    Collection: "auditlog"
    """
    actor: str = Field(..., description="Who performed the action")
    action: str = Field(..., description="Action description")
    entity: str = Field(..., description="Entity type (shipment, customer, etc.)")
    entity_id: Optional[str] = Field(None, description="Entity ID")
    metadata: Optional[dict] = Field(None, description="Additional metadata")

# The Flames database viewer can read these via GET /schema endpoint.
