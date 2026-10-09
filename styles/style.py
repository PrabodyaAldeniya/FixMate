from textwrap import dedent


def render_html(html):
    """Render HTML safely using dedent to prevent code block formatting issues."""
    st.markdown(dedent(html).strip(), unsafe_allow_html=True)


def get_css():
    return """
    <style>
    :root {
        --fixmate-navy: #0F2744;
        --fixmate-navy-2: #183B5B;
        --fixmate-orange: #F97316;
        --fixmate-orange-hover: #EA580C;
        --fixmate-bg: #F7F8FA;
        --fixmate-card: #FFFFFF;
        --fixmate-text: #10233F;
        --fixmate-muted: #667085;
        --fixmate-border: #E4E7EC;
        --fixmate-success: #12B76A;
        --fixmate-orange-bg: #FFF4ED;
        --fixmate-blue-bg: #F2F6FA;
        --fixmate-soft-white: #FFF;
    }

    .stApp {
        background-color: var(--fixmate-bg);
    }

    .block-container {
        max-width: 1240px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--fixmate-navy);
        font-weight: 700;
    }

    p, div {
        color: var(--fixmate-muted);
        font-size: 16px;
        line-height: 1.6;
    }

    a {
        color: var(--fixmate-navy);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s;
    }

    a:hover {
        color: var(--fixmate-orange);
    }

    .nav-link {
        color: var(--fixmate-text);
        font-weight: 500;
        text-decoration: none;
        transition: color 0.2s;
        padding: 8px 12px;
        border-radius: 6px;
    }

    .nav-link:hover {
        color: var(--fixmate-orange);
        background: var(--fixmate-soft-white);
    }

    .cta-primary {
        background: var(--fixmate-orange);
        color: var(--fixmate-soft-white);
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 16px;
        border: none;
        cursor: pointer;
        transition: background 0.2s;
    }

    .cta-primary:hover {
        background: var(--fixmate-orange-hover);
        color: var(--fixmate-soft-white);
    }

    .cta-secondary {
        background: var(--fixmate-card);
        color: var(--fixmate-navy);
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 16px;
        border: 1px solid var(--fixmate-border);
        cursor: pointer;
        transition: all 0.2s;
    }

    .cta-secondary:hover {
        background: var(--fixmate-orange);
        color: var(--fixmate-soft-white);
    }

    .card {
        background: var(--fixmate-card);
        border-radius: 16px;
        border: 1px solid var(--fixmate-border);
        padding: 24px;
        transition: box-shadow 0.2s;
    }

    .card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
    }

    .trust-card {
        background: var(--fixmate-card);
        border-radius: 12px;
        border: 1px solid var(--fixmate-border);
        padding: 20px;
        text-align: center;
        transition: transform 0.2s;
    }

    .trust-card:hover {
        transform: translateY(-2px);
    }

    .prof-card {
        background: var(--fixmate-card);
        border-radius: 16px;
        border: 1px solid var(--fixmate-border);
        padding: 24px;
        transition: box-shadow 0.2s;
    }

    .prof-card:hover {
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }

    .review-card {
        background: var(--fixmate-card);
        border-radius: 16px;
        border: 1px solid var(--fixmate-border);
        padding: 24px;
    }

    .section-title {
        font-size: 34px;
        font-weight: 700;
        color: var(--fixmate-navy);
        margin-top: 48px;
        margin-bottom: 24px;
    }

    .subheading {
        color: var(--fixmate-muted);
        font-size: 17px;
        margin-bottom: 32px;
    }

    .chip {
        display: inline-block;
        background: var(--fixmate-soft-white);
        color: var(--fixmate-text);
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
        margin-right: 8px;
        margin-bottom: 8px;
        transition: all 0.2s;
        border: 1px solid var(--fixmate-border);
    }

    .chip:hover {
        background: var(--fixmate-orange);
        color: var(--fixmate-soft-white);
    }

    .verified-badge {
        background: var(--fixmate-blue-bg);
        color: var(--fixmate-navy);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-top: 8px;
    }

    .rating-stars {
        color: var(--fixmate-orange);
        font-size: 20px;
    }

    .price-tag {
        color: var(--fixmate-orange);
        font-weight: 600;
    }

    .nav-button {
        background: transparent;
        color: var(--fixmate-muted);
        border: none;
        font-weight: 500;
        font-size: 14px;
        cursor: pointer;
        padding: 8px 16px;
        transition: all 0.2s;
    }

    .nav-button:hover {
        color: var(--fixmate-navy);
        border-bottom: 2px solid var(--fixmate-navy);
    }

    .stButton > button {
        transition: all 0.2s;
    }

    .stButton > button:hover {
        color: var(--fixmate-soft-white);
    }

    @media (max-width: 768px) {
        .block-container {
            max-width: 100%;
        }

        .section-title {
            font-size: 28px;
        }

        .chip {
            font-size: 12px;
            padding: 5px 8px;
        }
    }

    @media (max-width: 1024px) {
        .fixmate-header-inner {
            gap: 16px;
        }

        .fixmate-nav-link {
            font-size: 13px;
            padding: 6px 8px;
        }
    }

    @media (max-width: 640px) {
        .fixmate-header {
            padding: 0 0.5rem;
        }

        .fixmate-header-inner {
            gap: 8px;
        }

        .fixmate-logo {
            font-size: 18px;
        }

        .fixmate-nav {
            gap: 4px;
        }

        .fixmate-nav-link {
            font-size: 11px;
            padding: 4px 6px;
        }

        .fixmate-header-cta button {
            font-size: 12px;
            padding: 6px 12px;
            min-height: 36px;
        }
    }
    </style>
    """