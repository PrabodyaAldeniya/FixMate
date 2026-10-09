import base64
from pathlib import Path

import streamlit as st

from data.services import services
from data.professionals import professionals
from data.reviews import reviews
from styles.style import get_css


def get_logo_data_uri():
    """Load logo image from assets folder and return as data URI."""
    logo_path = Path(__file__).parent / "assets" / "fixmate_logo.png"
    if not logo_path.exists():
        return None
    encoded = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

# ==========================================
# PAGE CONFIGURATION
# ==========================================

logo_data_uri = get_logo_data_uri()
if logo_data_uri:
    page_icon = logo_data_uri
else:
    page_icon = "🛠️"

st.set_page_config(
    page_title="FixMate",
    page_icon=page_icon,
    layout="wide"
)

st.markdown(get_css(), unsafe_allow_html=True)


# ==========================================
# RENDER FUNCTIONS
# ==========================================


def render_navigation():
    """Render the navigation bar."""
    st.markdown("""
    <style>
    .fixmate-header {
        position: sticky;
        top: 0;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #E4E7EC;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 1rem;
    }

    .fixmate-header-inner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        max-width: 1240px;
        margin: 0 auto;
        gap: 24px;
        flex-wrap: nowrap;
    }

    .fixmate-logo-image {
        width: 52px;
        height: 52px;
        object-fit: contain;
        display: block;
        flex-shrink: 0;
    }

    .fixmate-logo-text {
        flex-shrink: 0;
        font-size: 40px;
        font-weight: 800;
        color: var(--fixmate-navy);
    }

    .fixmate-nav {
        display: flex;
        align-items: center;
        gap: 20px;
        flex-wrap: nowrap;
    }

    .fixmate-nav-link {
        white-space: nowrap;
        color: var(--fixmate-text);
        font-size: 15px;
        font-weight: 600;
        transition: color 0.2s;
    }

    .fixmate-nav-link:hover {
        color: var(--fixmate-orange);
    }

    .fixmate-header-cta {
        flex-shrink: 0;
        white-space: nowrap;
    }

    .fixmate-cta-btn {
        background: #F97316;
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        padding: 0 28px;
        min-height: 44px;
        font-size: 15px;
        transition: background 0.2s;
    }

    .fixmate-cta-btn:hover {
        background: #EA580C;
        color: #FFFFFF;
    }
    </style>

    <div class="fixmate-header">
        <div class="fixmate-header-inner">
            {f'<img src="{logo_data_uri}" class="fixmate-logo-image" alt="FixMate logo">' if logo_data_uri else ""}
            <div class="fixmate-logo-text">FixMate</div>
            <div class="fixmate-nav">
                <a href="#" class="fixmate-nav-link">Home</a>
                <a href="#" class="fixmate-nav-link">Services</a>
                <a href="#" class="fixmate-nav-link">How It Works</a>
                <a href="#" class="fixmate-nav-link">Professionals</a>
                <a href="#" class="fixmate-nav-link">Reviews</a>
            </div>
            <div class="fixmate-header-cta">
                <button class="fixmate-cta-btn">Book a Service</button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fixmate-header">
        <div class="fixmate-header-inner">
            {f'<img src="{logo_data_uri}" class="fixmate-logo-image" alt="FixMate logo">' if logo_data_uri else ""}
            <div class="fixmate-logo-text">FixMate</div>
            <div class="fixmate-nav">
                <a href="#" class="fixmate-nav-link">Home</a>
                <a href="#" class="fixmate-nav-link">Services</a>
                <a href="#" class="fixmate-nav-link">How It Works</a>
                <a href="#" class="fixmate-nav-link">Professionals</a>
                <a href="#" class="fixmate-nav-link">Reviews</a>
            </div>
            <div class="fixmate-header-cta">
                <button class="fixmate-cta-btn">Book a Service</button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_hero():
    """Render the hero section with service search."""
    left, right = st.columns([0.58, 0.42], gap="large")

    with left:
        st.title("Home repairs made")
        st.markdown(
            '<span style="color: var(--fixmate-orange);">simple, fast & reliable.</span>',
            unsafe_allow_html=True,
        )
        st.write(
            "Book verified professionals for repairs, maintenance, cleaning "
            "and home improvement — all in one place."
        )

        st.text_input(
            "What service do you need?",
            placeholder="Search electrical, plumbing, AC repair...",
            key="hero_search",
        )

        btn1, btn2 = st.columns(2)
        with btn1:
            st.button(
                "Find a Professional",
                type="primary",
                use_container_width=True,
                key="hero_book_professional",
            )
        with btn2:
            st.button(
                "Explore Services",
                use_container_width=True,
                key="hero_explore_services",
            )

    with right:
        prof = professionals[0]
        initials = prof['name'].split()[0][0] + prof['name'].split()[-1][0]
        st.markdown(
            f'''
            <div style="background: var(--fixmate-card); border-radius: 16px; border: 1px solid var(--fixmate-border); '
            f'padding: 24px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <div style="width: 64px; height: 64px; border-radius: 50%; '
                f'background: var(--fixmate-blue-bg); margin: 0 auto 16px; font-size: 24px; '
                f'line-height: 64px; display: inline-block; color: var(--fixmate-navy);">'
                f'{initials}</div>
                <div style="color: var(--fixmate-navy); font-size: 20px; font-weight: 700; margin-bottom: 4px;">'
                f'{prof["name"]}</div>
                <div style="color: var(--fixmate-muted); font-size: 15px; margin-bottom: 8px;">'
                f'{prof["profession"]}</div>
                <div style="margin: 8px 0;">
                    <span style="background: var(--fixmate-blue-bg); color: var(--fixmate-navy); padding: 4px 12px; '
                    'border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block; margin-right: 6px;">'
                    'Verified Professional</span>
                    <span style="color: var(--fixmate-orange); font-size: 22px; margin-left: 6;">★ {prof["rating"]}</span>
                </div>
                <div style="color: var(--fixmate-muted); font-size: 14px; margin-bottom: 12px;">'
                f'{prof["location"]}</div>
                <div style="margin-top: 12px;">
                    <span style="background: var(--fixmate-orange-bg); color: var(--fixmate-orange); padding: 4px 8px; '
                    'border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block; margin-right: 6px;">'
                    'Available Today</span>
                    <span style="color: var(--fixmate-muted); font-size: 14px;">'
                    f'{prof["experience"]}</span>
                </div>
                <div style="font-size: 18px; color: var(--fixmate-orange); font-weight: 700; margin-top: 12px;">'
                f'From {prof["starting_price"]}</div>
            </div>
            ''',
            unsafe_allow_html=True,
        )


def render_quick_service_categories():
    """Render quick service categories - kept once below hero."""
    st.write("")
    st.markdown("### Quick Service Categories")

    chip1, chip2, chip3, chip4 = st.columns(4)
    with chip1:
        st.markdown('<span class="chip">Electrical</span>', unsafe_allow_html=True)
    with chip2:
        st.markdown('<span class="chip">Plumbing</span>', unsafe_allow_html=True)
    with chip3:
        st.markdown('<span class="chip">AC Repair</span>', unsafe_allow_html=True)
    with chip4:
        st.markdown('<span class="chip">Cleaning</span>', unsafe_allow_html=True)


def render_trust_indicators_and_stats():
    """Render inline trust indicators below hero CTA and main statistics."""
    st.write("")

    st.markdown(
        '<div style="display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap;">'
        '<div style="background: var(--fixmate-blue-bg); color: var(--fixmate-navy); padding: 6px 12px; '
        'border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block;">'
        'Verified Experts</div>'
        '<div style="background: var(--fixmate-blue-bg); color: var(--fixmate-navy); padding: 6px 12px; '
        'border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block;">'
        'Transparent Pricing</div>'
        '<div style="background: var(--fixmate-blue-bg); color: var(--fixmate-navy); padding: 6px 12px; '
        'border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block;">'
        'Flexible Scheduling</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    stat1, stat2, stat3, stat4 = st.columns(4)

    with stat1:
        st.metric(
            label="Average Rating",
            value="4.9/5",
        )

    with stat2:
        st.metric(
            label="Verified Professionals",
            value="500+",
        )

    with stat3:
        st.metric(
            label="Completed Jobs",
            value="10K+",
        )

    with stat4:
        st.metric(
            label="Customer Satisfaction",
            value="98%",
        )


def render_popular_services():
    """Render popular services grid."""
    st.markdown("### Popular Services")
    st.write("Find trusted professionals for your everyday home service needs.")
    st.write("")

    for start in range(0, len(services), 4):
        columns = st.columns(4)
        current_services = services[start : start + 4]

        for column, service in zip(columns, current_services):
            with column:
                st.markdown(
                    '<div class="card" style="height: 100%; display: flex; flex-direction: column;">'
                    '<div style="font-size: 28px; margin-bottom: 16px;">'
                    f'{service["icon"]}'
                    '</div>'
                    '<h4 style="color: var(--fixmate-navy); font-size: 18px; margin-bottom: 8px;">'
                    f'{service["name"]}</h4>'
                    '<p style="color: var(--fixmate-muted); font-size: 14px; flex-grow: 1;">'
                    f'{service["short_description"]}</p>'
                    '<span class="price-tag" style="margin-top: 12px; display: block;">'
                    f'{service["starting_price"]}</span>'
                    '<div style="margin-top: 16px; align-self: flex-start;">'
                    '<a href="#" style="'
                    'color: var(--fixmate-orange);'
                    'font-weight: 600;'
                    'font-size: 14px;'
                    'text-decoration: underline;'
                    'transition: color 0.2s;">Explore Service →</a>'
                    '</div>'
                    '</div>',
                    unsafe_allow_html=True,
                )

def render_emergency_banner():
    """Render emergency service banner."""
    st.markdown(
        """
        <div style="background: var(--fixmate-orange-bg); padding: 24px; border-radius: 16px; 
                    margin: 24px 0; text-align: center; border-left: 4px solid var(--fixmate-orange);">
            <h3 style="color: var(--fixmate-orange-hover); font-size: 24px; margin-bottom: 8px;">
                Need urgent help?</h3>
            <p style="color: var(--fixmate-muted); font-size: 16px; margin-top: 0;">
                Find available professionals for urgent electrical, plumbing or home repair issues.</p>
            <div style="margin: 24px 0;">
                <button style="
                    background: var(--fixmate-orange); color: var(--fixmate-soft-white); padding: 12px 24px;
                    border-radius: 10px; font-weight: 600; font-size: 16px;
                    border: none; cursor: pointer; transition: background 0.2s;">
                    Find Emergency Help
                </button>
            </div>
            <p style="color: var(--fixmate-muted); font-size: 14px;">
                Frontend demo only - booking flow coming soon.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_how_it_works():
    """Render how fixate works steps."""
    st.markdown(
        '<h2 style="color: #10233F; font-size: 34px; margin-bottom: 24px;">'
        'Book a trusted professional in minutes.</h2>',
        unsafe_allow_html=True,
    )

    st.write("")

    step1, step2, step3, step4 = st.columns(4)

    with step1:
        st.markdown(
            '<div style="background: white; border-radius: 16px; border: 1px solid #E4E7EC;'
            'padding: 32px; text-align: center; height: 100%; min-height: 180px;">'
            '<div style="width: 56px; height: 56px; border-radius: 50px; background: #F97316;'
            'color: white; font-size: 32px; display: flex; align-items: center;'
            'justify-content: center; margin: 0 auto 20px; padding-top: 8px;">01</div>'
            '<h4 style="color: #10233F; font-size: 22px; margin-bottom: 8px;">Tell us</h4>'
            '<p style="color: #667085; font-size: 15px;">Tell us what you need</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    with step2:
        st.markdown(
            '<div style="background: white; border-radius: 16px; border: 1px solid #E4E7EC;'
            'padding: 32px; text-align: center; height: 100%; min-height: 180px;">'
            '<div style="width: 56px; height: 56px; border-radius: 50px; background: #F97316;'
            'color: white; font-size: 32px; display: flex; align-items: center;'
            'justify-content: center; margin: 0 auto 20px; padding-top: 8px;">02</div>'
            '<h4 style="color: #10233F; font-size: 22px; margin-bottom: 8px;">Choose</h4>'
            '<p style="color: #667085; font-size: 15px;">Choose your professional</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    with step3:
        st.markdown(
            '<div style="background: white; border-radius: 16px; border: 1px solid #E4E7EC;'
            'padding: 32px; text-align: center; height: 100%; min-height: 180px;">'
            '<div style="width: 56px; height: 56px; border-radius: 50px; background: #F97316;'
            'color: white; font-size: 32px; display: flex; align-items: center;'
            'justify-content: center; margin: 0 auto 20px; padding-top: 8px;">03</div>'
            '<h4 style="color: #10233F; font-size: 22px; margin-bottom: 8px;">Pick</h4>'
            '<p style="color: #667085; font-size: 15px;">Pick your time</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    with step4:
        st.markdown(
            '<div style="background: white; border-radius: 16px; border: 1px solid #E4E7EC;'
            'padding: 32px; text-align: center; height: 100%; min-height: 180px;">'
            '<div style="width: 56px; height: 56px; border-radius: 50px; background: #F97316;'
            'color: white; font-size: 32px; display: flex; align-items: center;'
            'justify-content: center; margin: 0 auto 20px; padding-top: 8px;">04</div>'
            '<h4 style="color: #10233F; font-size: 22px; margin-bottom: 8px;">Get</h4>'
            '<p style="color: #667085; font-size: 15px;">Get it done</p>'
            '</div>',
            unsafe_allow_html=True,
        )

def render_why_fixmate():
    """Render why FixMate section."""
    st.write("")
    st.markdown(
        '<div style="background: #F2F6FA; padding: 40px 24px; border-radius: 16px; '
        'margin: 32px 0;">'
        '<h2 style="color: #10233F; font-size: 34px; margin-bottom: 16px;">'
        'Why homeowners choose FixMate</h2>'
        '<p style="color: #667085; font-size: 17px; margin-bottom: 32px;">'
        'Trusted professionals, transparent pricing, and flexible scheduling.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="prof-card" style="height: 100%;">
                <div style="font-size: 28px; margin-bottom: 20px;">⚡</div>
                <h4 style="color: #10233F; font-size: 20px; margin-bottom: 8px;">Verified Professionals</h4>
                <p style="color: #667085; font-size: 15px; line-height: 1.5;">
                    All pros are screened and verified.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="prof-card" style="height: 100%;">
                <div style="background: #FFF4ED; border-radius: 12px; width: 48px; height: 48px; 
                    display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <span style="color: #EA580C; font-size: 20px;">₹</span>
                </div>
                <h4 style="color: #10233F; font-size: 20px; margin-bottom: 8px;">Transparent Pricing</h4>
                <p style="color: #667085; font-size: 15px; line-height: 1.5;">
                    Clear upfront costs with no hidden fees.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="prof-card" style="height: 100%;">
                <div style="background: #E7F5FF; border-radius: 12px; width: 48px; height: 48px; 
                    display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <span style="color: #0F2744; font-size: 20px;">⏰</span>
                </div>
                <h4 style="color: #10233F; font-size: 20px; margin-bottom: 8px;">Flexible Scheduling</h4>
                <p style="color: #667085; font-size: 15px; line-height: 1.5;">
                    Book appointments that fit your schedule.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="prof-card" style="height: 100%;">
                <div style="background: #E7F5FF; border-radius: 12px; width: 48px; height: 48px; 
                    display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <span style="color: #0F2744; font-size: 20px;">💬</span>
                </div>
                <h4 style="color: #10233F; font-size: 20px; margin-bottom: 8px;">Service Support</h4>
                <p style="color: #667085; font-size: 15px; line-height: 1.5;">
                    We're here if you need help after the job.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

def render_featured_professionals():
    """Render featured professionals grid."""
    st.write("")
    st.markdown("### Featured Professionals")

    for start in range(0, len(professionals), 3):
        columns = st.columns(3)
        current_profs = professionals[start : start + 3]

        for column, prof in zip(columns, current_profs):
            with column:
                initials = prof['name'].split()[0][0] + prof['name'].split()[-1][0]
                verified_badge = 'Verified Professional' if prof['verified'] else ''

                st.markdown(
                    f'''
                    <div class="prof-card" style="height: 100%; border: 1px solid var(--fixmate-border);
                        border-radius: 20px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <div style="width: 56px; height: 56px; border-radius: 50%; 
                            background: var(--fixmate-blue-bg); margin: 0 auto 16px; 
                            font-size: 20px; display: flex; align-items: center; 
                            justify-content: center; color: var(--fixmate-navy);">
                            {initials}
                        </div>
                        <div style="color: var(--fixmate-navy); font-size: 19px; font-weight: 700; 
                            margin-bottom: 4px;">{prof["name"]}</div>
                        <div style="color: var(--fixmate-muted); font-size: 14px; margin-bottom: 8px;">
                            {prof["profession"]}</div>
                        {f'<span style="background: var(--fixmate-blue-bg); color: var(--fixmate-navy); '
                         'padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600; '
                         'display: inline-block; margin-top: 8;">{verified_badge}</span>' if verified_badge else ""}
                        <div style="color: var(--fixmate-muted); font-size: 13px; margin-bottom: 4px;">
                            ★ {prof["rating"]} ({prof["review_count"]} reviews)</div>
                        <div style="color: var(--fixmate-muted); font-size: 13px; margin-bottom: 4px;">
                            📍 {prof["location"]}</div>
                        <div style="color: var(--fixmate-muted); font-size: 13px; margin-bottom: 4px;">
                            💪 {prof["experience"]}</div>
                        <div style="color: var(--fixmate-muted); font-size: 13px; margin-bottom: 4px;">
                            ✅ {prof["completed_jobs"]} completed jobs</div>
                        <div style="color: var(--fixmate-muted); font-size: 13px; margin-bottom: 12px;">
                            {prof["availability"]}</div>
                        <div style="color: var(--fixmate-orange); font-size: 15px; font-weight: 700;">
                            From {prof["starting_price"]}
                        </div>
                        <div style="display: flex; gap: 8px; margin-top: 16px;">
                            <button style="
                                background: #F97316; color: #FFFFFF; border: none; border-radius: 10px;
                                font-weight: 700; padding: 8px 16px; font-size: 14px;
                                transition: background 0.2s; flex: 1;">
                                Book Now
                            </button>
                            <button style="
                                background: transparent; color: var(--fixmate-navy); border: 1px solid var(--fixmate-navy);
                                border-radius: 10px; font-weight: 600; padding: 8px 16px; font-size: 14px;
                                transition: all 0.2s; flex: 1;">
                                View Profile
                            </button>
                        </div>
                    </div>
                    ''',
                    unsafe_allow_html=True,
                )


def render_customer_reviews():
    """Render customer reviews section."""
    st.write("")
    st.markdown("### Customer Reviews")
    st.write("")

    st.markdown(
        '<p style="color: #667085; font-size: 16px; margin-bottom: 24px;">'
        'Real experiences from customers who trusted FixMate.</p>',
        unsafe_allow_html=True,
    )

    for review in reviews:
        with st.container():
            customer_name = review.get("customer_name", "Customer")
            review_text = review.get("review", "")
            service_name = review.get("service", "")
            rating = review.get("rating", 5)
            date = review.get("date", "")

            st.markdown(
                f'<div style="background: white; border-radius: 16px; border: 1px solid #E4E7EC;'
                f'padding: 24px; min-height: 180px;">'
                f'<div style="display: flex; align-items: center; margin-bottom: 16px;">'
                f'<span style="color: #F97316; font-size: 24px;">★★★★★</span>'
                f'</div>'
                f'<p style="color: #667085; font-size: 15px; margin: 8px 0;">'
                f'{review_text}</p>'
                f'<div style="display: flex; justify-content: space-between; '
                f'align-items: center; color: #667085; font-size: 14px;">'
                f'<span>{customer_name}</span>'
                f'<span>{service_name} · {date}</span>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True,
            )


def render_trust_row():
    """Render trust/safety row before CTA."""
    st.write("")
    st.markdown(
        '<div style="background: #F7F8FA; padding: 16px 24px; border-radius: 12px; '
        'margin: 24px 0; border: 1px solid #E4E7EC; display: flex; justify-content: '
        'space-between; align-items: center; flex-wrap: wrap;">'
        '<span style="color: #667085; font-size: 14px;">Verified Professionals</span>'
        '<span style="color: #667085; font-size: 14px;">Secure Booking Process</span>'
        '<span style="color: #667085; font-size: 14px;">Transparent Pricing</span>'
        '<span style="color: #667085; font-size: 14px;">Customer Support</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_cta():
    """Render call-to-action section."""
    st.write("")

    st.markdown(
        '<div style="background: var(--fixmate-navy); padding: 32px 24px; '
        'border-radius: 16px; margin: 24px 0; color: white;">'
        '<h2 style="font-size: 34px; font-weight: 700; margin-bottom: 16px;">'
        'Need something fixed today?</h2>'
        '<p style="font-size: 18px; opacity: 0.9; margin-bottom: 24px;">'
        'Find a trusted professional and get your home back in shape.</p>',
        unsafe_allow_html=True,
    )

    st.write("")

    cta_left, cta_center, cta_right = st.columns([3, 2, 3])

    with cta_center:
        st.button(
            "Book a Service",
            type="primary",
            use_container_width=True,
            key="cta_book_service",
        )

    with cta_right:
        st.button(
            "Browse Services",
            use_container_width=True,
            key="cta_browse_services",
        )

    st.markdown(
        '<p style="background: var(--fixmate-orange); padding: 12px 24px; '
        'border-radius: 10px; margin: 24px 0; font-size: 14px; display: inline-block; '
        'color: var(--fixmate-navy);">'
        'No hidden fees • Verified experts • Flexible scheduling</p>',
        unsafe_allow_html=True,
    )


def render_footer():
    """Render the footer."""
    st.markdown(
        """
        <div style="background: var(--fixmate-navy); color: white; padding: 48px 24px 32px;
                    border-radius: 0 0 16px 16px;">
            <div style="display: flex; align-items: center; margin-bottom: 24px;">
                <span style="font-size: 24px; margin-right: 8px;">🛠️</span>
                <span style="font-size: 28px; font-weight: 700;">FixMate</span>
            </div>
            <p style="color: #98A2B3; font-size: 14px; line-height: 1.6;">
                Trusted home services, one click away.
            </p>
            <div style="display: flex; gap: 16px; margin-top: 32px; flex-wrap: wrap;">
                < 0
 0
  Vote: 
                <a href="#" style="color: #98A2B3; text-decoration: none; font-size: 14px;
                    transition: color 0.2s;">Electrical</a>
                <a href="#" style="color: #98A2B3; text-decoration: none; font-size: 14px;
                    transition: color 0.2s;">Plumbing</a>
                <a href="#" style="color: #98A2B3; text-decoration: none; font-size: 14px;
                    transition: color 0.2s;">AC Repair</a>
                <a href="#" style="color: #98A2B3; text-decoration: none; font-size: 14px;
                    transition: color 0.2s;">Cleaning</a>
            </div>
            <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid #E4E7EC;
                        color: #98A2B3; font-size: 13px; text-align: center;">
                © 2026 FixMate. All rights reserved.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
