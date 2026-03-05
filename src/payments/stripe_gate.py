import stripe
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

class StripeGate:
    def __init__(self):
        self.stripe = stripe
        
    def create_checkout_session(self, tier):
        try:
            # Define pricing tiers
            prices = {
                "free": "price_1234567890",
                "dev": "price_2345678901",
                "team": "price_3456789012"
            }
            
            if tier not in prices:
                raise ValueError(f"Invalid tier: {tier}")
            
            session = self.stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price": prices[tier],
                    "quantity": 1,
                }],
                mode="subscription",
                success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url="https://example.com/cancel"
            )
            
            return {
                "url": session.url
            }
        except Exception as e:
            print(f"[ERROR] Stripe checkout failed: {str(e)}")
            return None