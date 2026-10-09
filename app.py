import streamlit as st

from data.services import services
from data.professionals import professionals
from data.reviews import reviews
from styles.style import get_css

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="FixMate",
    page_icon="🛠️",
    layout="wide"
)

st.markdown(get_css(), unsafe_allow_html=True)


# ==========================================
# RENDER FUNCTIONS
# ==========================================


def render_navigation():
    """Render the navigation bar."""
    logo, menu, action = st.columns([2, 6, 2])

    with logo:
        st.title("FixMate")

    with menu:
        n1, n2, n3, n4, n5 = st.columns(5)
        with n1:
            st.button("Home", key="nav_home", help="Home", disabled=True)
        with n2:
            st.button("Services", key="nav_services", help="Services")
        with n3:
            st.button("Professionals", key="nav_professionals", help="Professionals")
        with n4:
            st.button("Reviews", key="nav_reviews", help="Reviews")
        with n5:
            st.button("How It Works", key="nav_how_it_works", help="How It Works")

    with action:
        st.button(
            "Book a Service",
            type="primary",
            use_container_width=True,
            key="navbar_book_service",
        )

    st.divider()


def render_hero():
    """Render the hero section with service search."""
    left, right = st.columns([1.15, 0.85], gap="large")

    with left:
        st.title("Home repairs made")
        st.subheader("simple, fast & reliable.")
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
        st.markdown("---")
        prof = professionals[0]
        st.markdown(f"### {prof['name']}")
        st.markdown(f"*{prof['profession']}*")
        badge = "Verified Professional" if prof.get("verified") else "Professional"
        st.caption(badge)
        st.caption(f"★ {prof['rating']} ({prof['review_count']} reviews)")
        st.caption(f"📍 {prof['location']}")
        st.caption(f"💪 {prof['experience']}")
        st.caption(f"✅ {prof['completed_jobs']} completed jobs")
        st.caption(f"🕒 {prof['availability']}")
        st.caption(f"From Rs. {prof['starting_price']}")


def render_quick_categories():
    """Render quick service categories."""
    st.write("")
    st.markdown("### Quick Service Categories")

    cat1, cat2, cat3, cat4 = st.columns(4)

    with cat1:
        st.button("Electrical", key="cat_electrical", use_container_width=True)
    with cat2:
        st.button("Plumbing", key="cat_plumbing", use_container_width=True)
    with cat3:
        st.button("AC Repair", key="cat_ac", use_container_width=True)
    with cat4:
        st.button("Cleaning", key="cat_cleaning", use_container_width=True)


def render_trust_statistics():
    """Render trust statistics cards."""
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

    for start in range(0, len(services), 3):
        columns = st.columns(3)
        current_services = services[start : start + 3]

        for column, service in zip(columns, current_services):
            with column:
                st.markdown(f"### {service['icon']} {service['name']}")
                st.write(service["short_description"])
                st.markdown(f"**Starting price: {service['starting_price']}**")
                st.button(
                    "Explore →",
                    key=f"service_{service['id']}",
                    use_container_width=True,
                )


def render_how_it_works():
    """Render how fixate works steps."""
    st.markdown("### How FixMate Works")
    st.write("Book trusted home services in simple steps.")
    st.write("")

    step1, step2, step3, step4 = st.columns(4)

    with step1:
        st.markdown("### 01")
        st.write("Tell us what you need")
        st.write("Select the repair or maintenance service your home needs.")

    with step2:
        st.markdown("### 02")
        st.write("Choose your professional")
        st.write("Choose a trusted professional based on skills and ratings.")

    with step3:
        st.markdown("### 03")
        st.write("Pick your time")
        st.write("Choose a convenient time slot for the service.")

    with step4:
        st.markdown("### 04")
        st.write("Get it done")
        st.write("The professional will handle the job at your location.")


def render_why_fixmate():
    """Render why fixate section."""
    st.write("")
    st.markdown("### Why FixMate")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            "**Verified Professionals**\n"
            "All pros are screened and verified."
        )

    with col2:
        st.markdown(
            "**Transparent Pricing**\n"
            "Clear upfront costs with no hidden fees."
        )

    with col3:
        st.markdown(
            "**Flexible Scheduling**\n"
            "Book appointments that fit your schedule."
        )

    with col4:
        st.markdown(
            "**Service Support**\n"
            "We're here if you need help after the job."
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
                initials = prof['name'].split()[0][0]
                st.markdown(f"**{prof['name']}**")
                st.markdown(f"*{prof['profession']}*")
                badge_color = "#0F2744" if prof.get("verified") else "#667085"
                st.markdown(
                    f'<span style="background: #E7F5FF; color: #0F2744; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; display: inline-block; margin-top: 8px;">Verified Professional</span>',
                    unsafe_allow_html=True,
                )
                st.caption(f"★ {prof['rating']} ({prof['review_count']} reviews)")
                st.caption(f"📍 {prof['location']}")
                st.caption(f"💪 {prof['experience']}")
                st.caption(f"✅ {prof['completed_jobs']} completed jobs")
                st.caption(f"🕒 {prof['availability']}")
                st.caption(f"From Rs. {prof['starting_price']}")
                st.button(
                    "View Profile",
                    key=f"prof_view_{prof['id']}",
                    use_container_width=True,
                )
                st.button(
                    "Book Now",
                    key=f"prof_book_{prof['id']}",
                    use_container_width=True,
                )


def render_customer_reviews():
    """Render customer reviews section."""
    st.write("")
    st.markdown("### Customer Reviews")

    for review in reviews:
        with st.container():
            review_text = review.get("review", "")
            st.markdown(f"> **{review_text}**")
            customer_name = review.get("customer_name", "Customer")
            service_name = review.get("service", "")
            rating = review.get("rating", 5)
            date = review.get("date", "")
            st.caption(f"{customer_name} · {service_name} · {date}")
            st.divider()


def render_cta():
    """Render call-to-action section."""
    st.write("")
    st.write("")

    st.markdown("### Need something fixed today?")
    st.write("Find a trusted professional and get your home back in shape.")

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


def render_footer():
    """Render the footer."""
    st.write("")
    st.divider()

    footer1, footer2, footer3, footer4 = st.columns([3, 2, 2, 2])

    with footer1:
        st.markdown("FixMate")
        st.write("Trusted home services, one click away.")

    with footer2:
        st.markdown("**Services**")
        st.write("Electrical")
        st.write("Plumbing")
        st.write("AC Repair")
        st.write("Carpentry")

    with footer3:
        st.markdown("**Company**")
        st.write("About")
        st.write("Careers")
        st.write("Press")

    with footer4:
        st.markdown("**Support**")
        st.write("Help Center")
        st.write("Contact")
        st.write("FAQ")

    st.divider()
    st.markdown("© 2026 FixMate. All rights reserved.")
    st.markdown("Privacy")
    st.markdown("Terms")


# ==========================================
# MAIN APPLICATION
# ==========================================

render_navigation()
render_hero()
render_quick_categories()
render_trust_statistics()
render_popular_services()
render_how_it_works()
render_why_fixmate()
render_featured_professionals()
render_customer_reviews()
render_cta()
render_footer()