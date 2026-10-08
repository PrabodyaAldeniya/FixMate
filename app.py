import streamlit as st

from data.services import services
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
            st.button("Home", key="nav_home", help="Home")
        with n2:
            st.button("Services", key="nav_services", help="Services")
        with n3:
            st.button("Professionals", key="nav_professionals", help="Professionals")
        with n4:
            st.button("Reviews", key="nav_reviews", help="Reviews")
        with n5:
            st.button("About", key="nav_about", help="About")

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
        st.title("Expert Home Services,")
        st.markdown("Right When You Need Them.")
        st.write(
            "Book trusted and verified professionals for repairs, "
            "maintenance and home improvement services."
        )
        st.write("Simple booking, reliable experts and transparent pricing.")

        btn1, btn2 = st.columns(2)
        with btn1:
            st.button(
                "Book a Service",
                type="primary",
                use_container_width=True,
                key="hero_book_service",
            )
        with btn2:
            st.button(
                "Explore Services",
                use_container_width=True,
                key="hero_explore_services",
            )

    with right:
        st.markdown("---")
        st.subheader("Trusted Home Services")
        st.write("Your home. Our trusted experts.")
        st.write(
            "FixMate connects you with skilled professionals "
            "for reliable and trusted home services."
        )


def render_trust_statistics():
    """Render trust statistics cards."""
    st.write("")
    st.write("")

    stat1, stat2, stat3 = st.columns(3)

    with stat1:
        st.metric(
            label="Customer Rating",
            value="4.9/5",
        )

    with stat2:
        st.metric(
            label="Verified Experts",
            value="500+",
        )

    with stat3:
        st.metric(
            label="Jobs Completed",
            value="10K+",
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


def render_how_it_works():
    """Render how fixate works steps."""
    st.markdown("### How FixMate Works")
    st.write("Book trusted home services in three simple steps.")
    st.write("")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.markdown("### 01")
        st.write("Choose a Service")
        st.write("Select the repair or maintenance service your home needs.")

    with step2:
        st.markdown("### 02")
        st.write("Pick a Professional")
        st.write("Choose a trusted professional based on skills and ratings.")

    with step3:
        st.markdown("### 03")
        st.write("Get It Fixed")
        st.write("Choose a convenient time and let the professional handle the job.")


def render_cta():
    """Render call-to-action section."""
    st.write("")
    st.write("")

    st.markdown("### Need something fixed today?")
    st.write("Book a trusted professional and get your home back in shape.")

    st.write("")
    cta_left, cta_center, cta_right = st.columns([3, 2, 3])

    with cta_center:
        st.button(
            "Book a Professional",
            type="primary",
            use_container_width=True,
            key="cta_book_professional",
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

    with footer3:
        st.markdown("**Company**")
        st.write("About")
        st.write("Professionals")
        st.write("Reviews")

    with footer4:
        st.markdown("**Support**")
        st.write("Help Center")
        st.write("Contact")
        st.write("FAQ")

    st.divider()
    st.markdown("© 2026 FixMate — Trusted Home Services, One Click Away.")


# ==========================================
# MAIN APPLICATION
# ==========================================

render_navigation()
render_hero()
render_trust_statistics()
render_popular_services()
render_how_it_works()
render_cta()
render_footer()