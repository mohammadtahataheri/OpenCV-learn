"""ParkVision desktop interface prototype."""

import customtkinter as ctk
from main import run_park

# ── App config ──────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_NAME = "ParkVision"
APP_VERSION = "v0.1.0"
WINDOW_WIDTH = 1160
WINDOW_HEIGHT = 760

# ── Colors ──────────────────────────────────────────────────────────
BG = "#0B0F19"
SIDEBAR = "#111827"
CARD = "#1F2937"
ACCENT = "#6366F1"
CYAN = "#22D3EE"
TEXT = "#F9FAFB"
MUTED = "#9CA3AF"
BORDER = "#334155"
SOFT = "#172033"
GREEN = "#34D399"

# ── Window ──────────────────────────────────────────────────────────
app = ctk.CTk()
app.title(f"{APP_NAME} — Workspace")
app.minsize(920, 680)

screen_x = max(0, (app.winfo_screenwidth() - WINDOW_WIDTH) // 2)
screen_y = max(0, (app.winfo_screenheight() - WINDOW_HEIGHT) // 2)
app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_x}+{screen_y}")

app.grid_columnconfigure(0, minsize=236)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.configure(fg_color=BG)

# ── Sidebar ─────────────────────────────────────────────────────────
sidebar = ctk.CTkFrame(
    app,
    fg_color=SIDEBAR,
    corner_radius=0,
    width=236
)
sidebar.grid(row=0, column=0, sticky="nsew")
sidebar.grid_propagate(False)
sidebar.grid_columnconfigure(0, weight=1)
sidebar.grid_rowconfigure(3, weight=1)

# Brand
brand = ctk.CTkFrame(sidebar, fg_color="transparent")
brand.grid(row=0, column=0, sticky="ew", padx=22, pady=(28, 32))
brand.grid_columnconfigure(1, weight=1)

brand_mark = ctk.CTkFrame(
    brand,
    width=42,
    height=42,
    fg_color=ACCENT,
    corner_radius=13
)
brand_mark.grid(row=0, column=0, rowspan=2, padx=(0, 11))
brand_mark.grid_propagate(False)

ctk.CTkLabel(
    brand_mark,
    text="P",
    text_color=TEXT,
    font=ctk.CTkFont(size=24, weight="bold")
).place(relx=0.5, rely=0.5, anchor="center")

ctk.CTkLabel(
    brand,
    text=APP_NAME,
    text_color=TEXT,
    font=ctk.CTkFont(size=18, weight="bold"),
    anchor="w"
).grid(row=0, column=1, sticky="ew")

ctk.CTkLabel(
    brand,
    text="VISION WORKSPACE",
    text_color=MUTED,
    font=ctk.CTkFont(size=9, weight="bold"),
    anchor="w"
).grid(row=1, column=1, sticky="ew")

# Nav label
ctk.CTkLabel(
    sidebar,
    text="WORKSPACE",
    text_color=MUTED,
    font=ctk.CTkFont(size=10, weight="bold"),
    anchor="w"
).grid(row=1, column=0, sticky="ew", padx=25, pady=(0, 12))

# Nav button (Home only)
nav = ctk.CTkFrame(sidebar, fg_color="transparent")
nav.grid(row=2, column=0, sticky="ew", padx=14)
nav.grid_columnconfigure(0, weight=1)

def switch_page(index):
    show_live_camera_page()
    app.after(150, run_park)

nav_btn = ctk.CTkButton(
    nav,
    text="⌂    Home",
    height=43,
    corner_radius=10,
    anchor="w",
    font=ctk.CTkFont(size=13, weight="bold"),
    fg_color=ACCENT,
    hover_color="#7779F4",
    text_color=TEXT,
    command=lambda: switch_page(0),
)
nav_btn.grid(row=0, column=0, sticky="ew", pady=3)

# Sidebar bottom
sidebar_bottom = ctk.CTkFrame(sidebar, fg_color="transparent")
sidebar_bottom.grid(row=4, column=0, sticky="ew", padx=14, pady=(0, 22))
sidebar_bottom.grid_columnconfigure(0, weight=1)

ctk.CTkFrame(
    sidebar_bottom,
    height=1,
    fg_color=BORDER
).grid(row=0, column=0, sticky="ew", padx=8, pady=(0, 15))

ctk.CTkButton(
    sidebar_bottom,
    text="⚙    Preferences",
    height=42,
    corner_radius=10,
    anchor="w",
    fg_color="transparent",
    hover_color=CARD,
    text_color=MUTED,
    font=ctk.CTkFont(size=13),
).grid(row=1, column=0, sticky="ew")

ctk.CTkLabel(
    sidebar_bottom,
    text=f"{APP_NAME}  {APP_VERSION}",
    text_color=MUTED,
    font=ctk.CTkFont(size=10),
    anchor="w",
).grid(row=2, column=0, sticky="ew", padx=15, pady=(17, 0))

# ── Header ──────────────────────────────────────────────────────────
workspace = ctk.CTkFrame(app, fg_color=BG, corner_radius=0)
workspace.grid(row=0, column=1, sticky="nsew")
workspace.grid_columnconfigure(0, weight=1)
workspace.grid_rowconfigure(1, weight=1)

header = ctk.CTkFrame(
    workspace,
    fg_color=BG,
    corner_radius=0,
    height=92
)
header.grid(row=0, column=0, sticky="ew", padx=32)
header.grid_propagate(False)
header.grid_columnconfigure(0, weight=1)

header_title = ctk.CTkLabel(
    header,
    text="Home",
    text_color=TEXT,
    font=ctk.CTkFont(size=23, weight="bold"),
    anchor="w"
)
header_title.grid(row=0, column=0, sticky="w", pady=(20, 18))

header_sub = ctk.CTkLabel(
    header,
    text="Your parking vision workspace at a glance",
    text_color=MUTED,
    font=ctk.CTkFont(size=12),
    anchor="w"
)
header_sub.grid(row=1, column=0, sticky="w", pady=(0, 18))

header_tools = ctk.CTkFrame(header, fg_color="transparent")
header_tools.grid(row=0, column=1, sticky="e", rowspan=2)

ctk.CTkEntry(
    header_tools,
    width=190,
    height=36,
    placeholder_text="⌕  Search workspace",
    fg_color=SIDEBAR,
    border_color=BORDER,
    border_width=1,
    corner_radius=9,
    text_color=TEXT,
    placeholder_text_color=MUTED,
    font=ctk.CTkFont(size=12),
).grid(row=0, column=0, padx=(0, 11))

ctk.CTkButton(
    header_tools,
    text="⚙",
    width=36,
    height=36,
    corner_radius=9,
    fg_color=SIDEBAR,
    hover_color=CARD,
    border_width=1,
    border_color=BORDER,
    text_color=TEXT,
    font=ctk.CTkFont(size=17),
).grid(row=0, column=1, padx=(0, 16))

status = ctk.CTkFrame(header_tools, fg_color=SOFT, corner_radius=9)
status.grid(row=0, column=2)

ctk.CTkLabel(status, text="●", text_color=GREEN, font=ctk.CTkFont(size=11)).grid(row=0, column=0, padx=(11, 6), pady=8)
ctk.CTkLabel(status, text="Ready", text_color=TEXT, font=ctk.CTkFont(size=11, weight="bold")).grid(row=0, column=1, padx=(0, 11), pady=8)

# ── Content area ────────────────────────────────────────────────────
content = ctk.CTkScrollableFrame(
    workspace,
    fg_color=BG,
    corner_radius=0,
    scrollbar_button_color=BORDER,
    scrollbar_button_hover_color=ACCENT,
)
content.grid(row=1, column=0, sticky="nsew", padx=16, pady=16)
content.grid_columnconfigure(0, weight=1)
content.grid_rowconfigure(0, weight=1)

live_camera_card = None


def show_live_camera_page():
    """Build a single full-size Live Camera card."""
    global live_camera_card

    for w in content.winfo_children():
        w.destroy()

    live_camera_card = ctk.CTkFrame(
        content,
        fg_color=CARD,
        corner_radius=16,
        border_width=1,
        border_color=BORDER,
    )
    live_camera_card.grid(row=0, column=0, sticky="nsew")
    live_camera_card.grid_columnconfigure(0, weight=1)
    live_camera_card.grid_rowconfigure(1, weight=1)

    # Card heading
    ctk.CTkLabel(
        live_camera_card,
        text="◉  Live Camera",
        text_color=TEXT,
        font=ctk.CTkFont(size=15, weight="bold"),
        anchor="w",
    ).grid(row=0, column=0, sticky="ew", padx=20, pady=(18, 12))

    # Feed placeholder area
    feed_area = ctk.CTkFrame(live_camera_card, fg_color=SOFT, corner_radius=12)
    feed_area.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
    feed_area.grid_columnconfigure(0, weight=1)
    feed_area.grid_rowconfigure(0, weight=1)

    ctk.CTkLabel(
        feed_area,
        text="Camera feed will appear here\n\nPress 'View Camera' below to start",
        text_color=MUTED,
        font=ctk.CTkFont(size=13),
        anchor="center",
    ).pack(expand=True, fill="both")

    # View Camera button
    ctk.CTkButton(
        live_camera_card,
        text="View Camera  →",
        width=140,
        height=38,
        corner_radius=9,
        fg_color=ACCENT,
        hover_color="#7779F4",
        text_color=TEXT,
        font=ctk.CTkFont(size=12, weight="bold"),
        command=run_park,
    ).grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 16))


# ── Footer ──────────────────────────────────────────────────────────
footer = ctk.CTkFrame(
    workspace,
    fg_color=BG,
    corner_radius=0,
    height=43
)
footer.grid(row=2, column=0, sticky="ew", padx=32)
footer.grid_propagate(False)
footer.grid_columnconfigure(0, weight=1)

ctk.CTkFrame(footer, height=1, fg_color=BORDER).grid(row=0, column=0, columnspan=2, sticky="ew")

ctk.CTkLabel(
    footer,
    text=f"© 2026 {APP_NAME} · Desktop workspace",
    text_color=MUTED,
    font=ctk.CTkFont(size=10),
    anchor="w",
).grid(row=1, column=0, sticky="w", pady=(8, 0))

ctk.CTkLabel(
    footer,
    text="Interface preview",
    text_color=MUTED,
    font=ctk.CTkFont(size=10),
    anchor="e",
).grid(row=1, column=1, sticky="e", pady=(8, 0))

# ── Startup ─────────────────────────────────────────────────────────
show_live_camera_page()

if __name__ == "__main__":
    app.mainloop()
