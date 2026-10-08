from textwrap import dedent


def render_html(html):
    """Render HTML safely using dedent to prevent code block formatting issues."""
    st.markdown(dedent(html).strip(), unsafe_allow_html=True)


def get_css():
    return """
    <style>

    .stApp {
        background-color: #F7F8FA;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #10233F;
    }

    .nav-link {
        color: #667085;
        font-weight: 500;
        text-decoration: none;
        transition: color 0.2s;
    }

    .nav-link:hover {
        color: #0F2744;
    }

    .cta-primary {
        background: #0F2744;
        color: white;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 16px;
        border: none;
        cursor: pointer;
        transition: background 0.2s;
    }

    .cta-primary:hover {
        background: #F97316;
        color: #0F2744;
    }

    .cta-secondary {
        background: transparent;
        color: #0F2744;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 16px;
        border: 1px solid #0F2744;
        cursor: pointer;
        transition: all 0.2s;
    }

    .cta-secondary:hover {
        background: #F97316;
        color: #0F2744;
    }

    .card {
        background: white;
        border-radius: 16px;
        border: 1px solid #E7E9EE;
        padding: 24px;
        transition: box-shadow 0.2s;
    }

    .card:hover {
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
    }

    .trust-card {
        background: white;
        border-radius: 12px;
        border: 1px solid #E7E9EE;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s;
    }

    .trust-card:hover {
        transform: translateY(-2px);
    }

    .prof-card {
        background: white;
        border-radius: 12px;
        border: 1px solid #E7E9EE;
        padding: 20px;
        transition: box-shadow 0.2s;
    }

    .prof-card:hover {
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }

    .review-card {
        background: white;
        border-radius: 12px;
        border: 1px solid #E7E9EE;
        padding: 20px;
    }

    .section-title {
        font-size: 32px;
        font-weight: 700;
        color: #10233F;
        margin-top: 40px;
        margin-bottom: 20px;
    }

    .subheading {
        color: #667085;
        font-size: 16px;
        margin-bottom: 35px;
    }

    .chip {
        display: inline-block;
        background: #F7F8FA;
        color: #667085;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
        margin-right: 6px;
        margin-bottom: 6px;
        transition: all 0.2s;
    }

    .chip:hover {
        background: #0F2744;
        color: white;
    }

    .verified-badge {
        background: #E7F5FF;
        color: #0F2744;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-top: 8px;
    }

    .rating-stars {
        color: #F97316;
        font-size: 18px;
    }

    .price-tag {
        color: #F97316;
        font-weight: 600;
    }

    .nav-button {
        background: transparent;
        color: #667085;
        border: none;
        font-weight: 500;
        font-size: 14px;
        cursor: pointer;
        padding: 8px 16px;
        transition: all 0.2s;
    }

    .nav-button:hover {
        color: #0F2744;
        border-bottom: 2px solid #0F2744;
    }

    @media (max-width: 768px) {
        .block-container {
            max-width: 100%;
        }

        .hero-title {
            font-size: 32px;
        }

        .section-title {
            font-size: 24px;
        }

        .chip {
            font-size: 11px;
            padding: 5px 8px;
        }
    }

    </style>
    """