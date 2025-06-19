            "webhook notifications"
        ],
        "apis_required": {
            "openai": "GPT-4 for facts, verification, SEO",
            "anthropic": "Claude Sonnet for article writing", 
            "firecrawl": "Content extraction from URLs",
            "brave": "News search (only for topic queries)"
        },
        "real_implementation": True,
        "no_mocks": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
