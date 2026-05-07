import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Sistem Pakar Investasi Keuangan",
    page_icon="SP",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background: #ffffff;
    color: #111111;
}

html, body, [class*="css"] {
    color: #111111;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2.5rem;
}

.sp-banner {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #eff6ff 0%, #f5f3ff 55%, #ecfeff 100%);
    border: 1px solid #dbeafe;
    border-radius: 24px;
    padding: 30px 24px;
    color: #111111;
    text-align: center;
    margin-bottom: 22px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
}

.sp-banner::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(120deg, rgba(255,255,255,0.70), transparent 40%, rgba(255,255,255,0.18));
    pointer-events: none;
}

.sp-badge-row {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 16px;
    position: relative;
    z-index: 1;
}

.sp-badge {
    font-size: 12px;
    letter-spacing: .6px;
    text-transform: uppercase;
    font-weight: 800;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.75);
    border: 1px solid rgba(37,99,235,0.14);
    color: #1e3a8a;
}

.sp-banner h1 {
    font-size: 38px;
    font-weight: 900;
    margin-bottom: 10px;
    color: #0f172a;
    line-height: 1.08;
    letter-spacing: -0.04em;
    position: relative;
    z-index: 1;
}

.sp-banner p {
    font-size: 16px;
    opacity: 0.95;
    margin: 0;
    color: #475569;
    line-height: 1.7;
    position: relative;
    z-index: 1;
}

.sp-card {
    background: #ffffff;
    border: 1px solid #dbe3ee;
    border-radius: 18px;
    padding: 24px 26px;
    margin-bottom: 16px;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.05);
}

.sp-section-hd {
    font-size: 20px;
    font-weight: 800;
    margin: 18px 0 12px;
    padding-bottom: 8px;
    border-bottom: 2px solid #1d4ed8;
    display: inline-block;
    color: #0f172a;
}

.sp-step-lbl {
    font-size: 13px;
    opacity: .82;
    text-transform: uppercase;
    letter-spacing: 1.1px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #64748b;
}

.sp-q-text {
    font-size: 25px;
    font-weight: 850;
    margin-bottom: 10px;
    line-height: 1.35;
    color: #0f172a;
    width: 100%;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    letter-spacing: -0.02em;
}

.sp-q-hint {
    font-size: 15px;
    opacity: .9;
    font-style: normal;
    margin-bottom: 0;
    line-height: 1.75;
    color: #64748b;
    width: 100%;
    text-align: center;
}

.sp-formula {
    font-family: 'Courier New', monospace;
    font-size: 14px;
    background: #f8fafc;
    border-radius: 10px;
    padding: 12px 14px;
    margin-top: 10px;
    line-height: 1.7;
    border-left: 4px solid #1d4ed8;
    color: #0f172a;
    border: 1px solid #dbe3ee;
}

.sp-res-banner {
    position: relative;
    overflow: hidden;
    border-radius: 18px;
    padding: 28px 24px;
    text-align: center;
    color: #ffffff;
    margin-bottom: 16px;
    box-shadow: 0 14px 30px rgba(15, 23, 42, .16);
    border: 1px solid rgba(255,255,255,.16);
}

.sp-res-banner::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(120deg, rgba(255,255,255,0.18), transparent 45%, transparent 65%, rgba(255,255,255,0.06));
    pointer-events: none;
}

.sp-res-lbl {
    font-size: 13px;
    letter-spacing: 1.2px;
    opacity: .92;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-weight: 700;
}

.sp-res-title {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 8px;
}

.sp-res-inst {
    font-size: 16px;
    opacity: .96;
    line-height: 1.6;
}

.sp-cf-card {
    background: #ffffff;
    border: 1px solid #dbe3ee;
    border-radius: 18px;
    padding: 18px 20px;
    margin-bottom: 14px;
}

.sp-gauge-track {
    height: 10px;
    background: #e5e7eb;
    border-radius: 5px;
    overflow: hidden;
    margin: 6px 0 3px;
}

.sp-gauge-fill { height: 100%; border-radius: 5px; transition: width .5s; }
.sp-gauge-lbls { display: flex; justify-content: space-between; font-size: 11px; opacity: .7; color: #111111; }

.sp-wm-table { width: 100%; border-collapse: collapse; }
.sp-wm-table tr { border-bottom: 1px solid #e2e8f0; }
.sp-wm-table tr:last-child { border-bottom: none; }
.sp-wm-table td { padding: 10px 4px; font-size: 15px; color: #111111; }

.sp-wm-key { opacity: .9; }
.sp-wm-val { font-weight: 700; text-align: right; }
.sp-wm-cf { color: #1d4ed8; font-size: 13px; font-weight: 700; text-align: right; padding-left: 8px; }

.sp-tip {
    padding: 9px 0;
    border-bottom: 1px solid #e2e8f0;
    font-size: 15px;
    line-height: 1.6;
    display: flex;
    gap: 10px;
    color: #111111;
}

.sp-tip:last-child { border-bottom: none; }
.sp-tip-ck { color: #16a34a; flex-shrink: 0; }

.sp-warn {
    background: #fffbeb;
    border: 1px solid #f59e0b;
    border-radius: 10px;
    padding: 11px 14px;
    font-size: 14px;
    color: #92400e;
    margin-bottom: 12px;
}

.sp-log {
    background: #f8fafc;
    border-radius: 10px;
    padding: 14px 16px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    white-space: pre-wrap;
    max-height: 240px;
    overflow-y: auto;
    line-height: 1.8;
    border: 1px solid #d1d5db;
    color: #111111;
}

.sp-intro-item {
    padding: 10px 0;
    border-bottom: 1px solid #e2e8f0;
    font-size: 15px;
    display: flex;
    gap: 10px;
    line-height: 1.6;
    color: #111111;
}

.sp-intro-item:last-child { border-bottom: none; }

.sp-option-box {
    background: #f9fafb;
    border: 1px solid #d1d5db;
    border-left: 5px solid #1d4ed8;
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 12px;
    line-height: 1.7;
    color: #111111;
    font-size: 15px;
}

.option-save {
    border: 2px solid #dc2626;
}

.option-low {
    border: 2px solid #f97316;
}

.option-medium {
    border: 2px solid #eab308;
}

.option-high {
    border: 2px solid #16a34a;
}

.sp-option-title {
    font-size: 16px;
    font-weight: 800;
    margin-bottom: 6px;
    color: #111111;
}

.stRadio label, .stSelectSlider label {
    font-size: 15px !important;
    color: #111111 !important;
}

div[data-testid="stRadio"],
div[data-testid="stSelectSlider"] {
    background: #ffffff;
    padding: 10px 12px;
    border-radius: 16px;
    border: 1px solid #dbe3ee;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
}

div[data-testid="stRadio"] {
    width: fit-content;
    margin: 0 auto;
    text-align: center;
}

div[data-testid="stRadio"] > div {
    justify-content: center;
}

div[data-testid="stRadio"] label {
    justify-content: center;
}

div[data-testid="stRadio"] *,
div[data-testid="stSelectSlider"] * {
    color: #111111 !important;
    font-size: 15px !important;
}

div[data-testid="stButton"] {
    display: block;
}

div[data-testid="stButton"] > button {
    width: 100%;
    min-width: 180px;
    border-radius: 14px;
    font-weight: 800;
    font-size: 16px;
    padding: 12px 20px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    box-shadow: 0 10px 22px rgba(37,99,235,.18);
    transition: all .2s ease;
}

div[data-testid="stButton"] > button:hover {
    background: linear-gradient(135deg, #1d4ed8, #6d28d9);
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 14px 28px rgba(37,99,235,.24);
}

div[data-testid="stExpander"] {
    border: 1px solid #d1d5db;
    border-radius: 14px;
    background: #ffffff;
    overflow: hidden;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
}

div[data-testid="stExpander"] summary {
    font-size: 16px;
    font-weight: 700;
    color: #111111;
}

div[data-testid="stProgress"] > div {
    background: #e5e7eb;
    border-radius: 999px;
    height: 10px;
}

div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #22c55e, #2563eb, #7c3aed);
    border-radius: 999px;
}

@media (max-width: 640px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .sp-banner h1 { font-size: 30px; }
    .sp-q-text { font-size: 21px; }
    .sp-intro-item { flex-direction: column; }
}
</style>
""", unsafe_allow_html=True)

def cf_and(*cfs):
    return min(cfs)

def cf_rule(cf_ev, cf_r):
    return round(cf_ev * cf_r, 4)

def cf_combine(a, b):
    if a >= 0 and b >= 0:
        return round(a + b * (1 - a), 4)
    elif a < 0 and b < 0:
        return round(a + b * (1 + a), 4)
    else:
        return round((a + b) / (1 - min(abs(a), abs(b))), 4)

def cf_label(cf):
    if cf >= 0.8:
        return "Almost Certainly"
    if cf >= 0.6:
        return "Probably"
    if cf >= 0.4:
        return "Maybe"
    return "Weak"

RULE_CF = {
    "R5": 1.0, "R6": 1.0, "R7": 1.0, "R8": 1.0,
    "R9": 1.0, "R10": 0.9, "R11": 0.9, "R12": 0.9,
    "R13": 0.8, "R14": 0.8, "R15": 0.9,
    "R1": 0.9, "R2": 0.9, "R3": 0.9, "R4": 1.0,
}

def run_inference(facts):
    wm = {}
    log = []

    def wm_set(var, val, cf, src):
        wm[var] = (val, cf)
        log.append(f"[WM] {var} = {val}  (CF={cf})  <- {src}")

    for var, (val, cf) in facts.items():
        wm_set(var, val, cf, "User input")

    log.append("\nRule Set 2: Kesiapan Investasi")
    ps_v, ps_c = wm["pendapatan_stabil"]
    dd_v, dd_c = wm["dana_darurat"]
    uk_v, uk_c = wm["utang_konsumtif"]

    if ps_v == "Tidak":
        cf = cf_rule(ps_c, RULE_CF["R8"])
        log.append(f"R8: Pendapatan=Tidak -> Tidak Siap  CF={ps_c} x {RULE_CF['R8']} = {cf}")
        kv, kc = "Tidak Siap", cf
    elif dd_v == "Tidak":
        cf = cf_rule(cf_and(ps_c, dd_c), RULE_CF["R7"])
        log.append(f"R7: Stabil=Ya & Dana=Tidak -> Tidak Siap  CF={cf}")
        kv, kc = "Tidak Siap", cf
    elif uk_v == "Ya":
        cf = cf_rule(cf_and(ps_c, dd_c, uk_c), RULE_CF["R6"])
        log.append(f"R6: Stabil=Ya & Dana=Ya & Utang=Ya -> Tidak Siap  CF={cf}")
        kv, kc = "Tidak Siap", cf
    else:
        cf = cf_rule(cf_and(ps_c, dd_c, uk_c), RULE_CF["R5"])
        log.append(f"R5: Stabil=Ya & Dana=Ya & Utang=Tidak -> Siap  CF={cf}")
        kv, kc = "Siap", cf
    wm_set("kesiapan_investasi", kv, kc, "Rule Set 2")

    log.append("\nRule Set 3: Profil Risiko")
    lk_v, lk_c = wm["literasi_keuangan"]
    tr_v, tr_c = wm["toleransi_risiko"]
    cands = {}

    def push(k, cf):
        cands.setdefault(k, []).append(cf)

    if tr_v == "Rendah":
        cf = cf_rule(tr_c, RULE_CF["R9"])
        log.append(f"R9: Toleransi=Rendah -> Profil Rendah  CF={cf}")
        push("Rendah", cf)
    if lk_v == "Rendah" and tr_v == "Sedang":
        cf = cf_rule(cf_and(lk_c, tr_c), RULE_CF["R10"])
        log.append(f"R10 -> Profil Rendah  CF={cf}")
        push("Rendah", cf)
    if lk_v == "Sedang" and tr_v == "Sedang":
        cf = cf_rule(cf_and(lk_c, tr_c), RULE_CF["R11"])
        log.append(f"R11 -> Profil Sedang  CF={cf}")
        push("Sedang", cf)
    if lk_v == "Tinggi" and tr_v == "Sedang":
        cf = cf_rule(cf_and(lk_c, tr_c), RULE_CF["R12"])
        log.append(f"R12 -> Profil Sedang  CF={cf}")
        push("Sedang", cf)
    if lk_v == "Rendah" and tr_v == "Tinggi":
        cf = cf_rule(cf_and(lk_c, tr_c), RULE_CF["R13"])
        log.append(f"R13 -> Profil Sedang  CF={cf}")
        push("Sedang", cf)
    if lk_v == "Sedang" and tr_v == "Tinggi":
        cf = cf_rule(cf_and(lk_c, tr_c), RULE_CF["R14"])
        log.append(f"R14 -> Profil Sedang  CF={cf}")
        push("Sedang", cf)
    if lk_v == "Tinggi" and tr_v == "Tinggi":
        cf = cf_rule(cf_and(lk_c, tr_c), RULE_CF["R15"])
        log.append(f"R15 -> Profil Tinggi  CF={cf}")
        push("Tinggi", cf)

    pv, pc = None, 0.0
    for k, lst in cands.items():
        acc = lst[0]
        for x in lst[1:]:
            acc = cf_combine(acc, x)
        if acc > pc:
            pv, pc = k, acc
    wm_set("profil_risiko", pv, pc, "Rule Set 3")

    log.append("\nRule Set 1: Rekomendasi Investasi")
    ki_v, ki_c = wm["kesiapan_investasi"]
    pr_v, pr_c = wm["profil_risiko"]

    if ki_v == "Tidak Siap":
        cf = cf_rule(ki_c, RULE_CF["R4"])
        log.append(f"R4: Tidak Siap -> Fokus Menabung  CF={cf}")
        rk, rc = "fokus_menabung", cf
    elif pr_v == "Rendah":
        cf = cf_rule(cf_and(ki_c, pr_c), RULE_CF["R1"])
        log.append(f"R1: Siap & Profil=Rendah -> Risiko Rendah  CF={cf}")
        rk, rc = "risiko_rendah", cf
    elif pr_v == "Sedang":
        cf = cf_rule(cf_and(ki_c, pr_c), RULE_CF["R2"])
        log.append(f"R2: Siap & Profil=Sedang -> Risiko Sedang  CF={cf}")
        rk, rc = "risiko_sedang", cf
    else:
        cf = cf_rule(cf_and(ki_c, pr_c), RULE_CF["R3"])
        log.append(f"R3: Siap & Profil=Tinggi -> Risiko Tinggi  CF={cf}")
        rk, rc = "risiko_tinggi", cf

    wm_set("rekomendasi", REC[rk]["label"], rc, "Rule Set 1")
    return rk, rc, wm, log

REC = {
    "fokus_menabung": {
        "label": "Fokus Menabung",
        "title": "Belum Siap Berinvestasi",
        "instrument": "Prioritaskan membangun dana darurat dan stabilitas keuangan",
        "bg": "linear-gradient(135deg,#dc2626,#ef4444)",
        "tips": [
            "Lunasi seluruh utang konsumtif terlebih dahulu",
            "Bangun dana darurat minimal 3x pengeluaran bulanan",
            "Pastikan pendapatan stabil minimal 6 bulan berturut-turut",
            "Catat pemasukan dan pengeluaran setiap hari",
        ],
    },
    "risiko_rendah": {
        "label": "Risiko Rendah",
        "title": "Instrumen Konservatif",
        "instrument": "Tabungan Berjangka, Deposito, Reksa Dana Pasar Uang",
        "bg": "linear-gradient(135deg,#ea580c,#f97316)",
        "tips": [
            "Mulai dengan deposito berjangka 3 sampai 6 bulan",
            "Reksa Dana Pasar Uang cocok untuk likuiditas tinggi",
            "Imbal hasil stabil sekitar 4 sampai 6 persen per tahun",
            "Cocok untuk dana yang mungkin dibutuhkan jangka pendek",
        ],
    },
    "risiko_sedang": {
        "label": "Risiko Sedang",
        "title": "Instrumen Moderat",
        "instrument": "Reksa Dana Campuran, Reksa Dana Pendapatan Tetap",
        "bg": "linear-gradient(135deg,#ca8a04,#eab308)",
        "tips": [
            "Reksa Dana Campuran menyeimbangkan return dan risiko",
            "Reksa Dana Pendapatan Tetap cocok untuk horizon 2 sampai 5 tahun",
            "Diversifikasi ke minimal 2 jenis instrumen",
            "Review portofolio setiap 3 sampai 6 bulan",
        ],
    },
    "risiko_tinggi": {
        "label": "Risiko Tinggi",
        "title": "Instrumen Agresif",
        "instrument": "Saham, Aset Kripto",
        "bg": "linear-gradient(135deg,#15803d,#16a34a)",
        "tips": [
            "Gunakan hanya dana yang benar-benar siap untuk rugi",
            "Lakukan riset fundamental sebelum membeli saham",
            "Batasi alokasi aset kripto maksimal 10 sampai 15 persen total portofolio",
            "Terapkan stop-loss dan manajemen risiko yang ketat",
        ],
    },
}

QUESTIONS = [
    {
        "id": "pendapatan_stabil",
        "label": "Stabilitas Pendapatan",
        "text": "Apakah pendapatan Anda sudah stabil?",
        "hint": "Stabil berarti diterima rutin setiap bulan dan konsisten minimal 6 bulan berturut-turut.",
        "options": ["Ya", "Tidak"],
    },
    {
        "id": "dana_darurat",
        "label": "Dana Darurat",
        "text": "Apakah Anda memiliki dana darurat?",
        "hint": "Minimal 3x pengeluaran bulanan dan mudah dicairkan kapan saja.",
        "options": ["Ya", "Tidak"],
    },
    {
        "id": "utang_konsumtif",
        "label": "Utang Konsumtif",
        "text": "Apakah Anda memiliki utang konsumtif saat ini?",
        "hint": "Kartu kredit, pinjol, cicilan barang non-aset, dan sejenisnya.",
        "options": ["Ya", "Tidak"],
    },
    {
        "id": "literasi_keuangan",
        "label": "Literasi Keuangan",
        "text": "Bagaimana tingkat literasi keuangan Anda?",
        "hint": "Rendah: belum paham anggaran dan risiko. Sedang: paham tabungan dan investasi dasar. Tinggi: mampu analisis risiko dan rencana mandiri.",
        "options": ["Rendah", "Sedang", "Tinggi"],
    },
    {
        "id": "toleransi_risiko",
        "label": "Toleransi Risiko",
        "text": "Bagaimana toleransi risiko investasi Anda?",
        "hint": "Rendah: hindari kerugian. Sedang: sedikit rugi masih ok. Tinggi: siap hadapi fluktuasi besar demi return tinggi.",
        "options": ["Rendah", "Sedang", "Tinggi"],
    },
]

CF_OPTIONS = {
    "Kurang Yakin  (CF = 0.4)": 0.4,
    "Cukup Yakin   (CF = 0.6)": 0.6,
    "Yakin         (CF = 0.8)": 0.8,
    "Sangat Yakin  (CF = 1.0)": 1.0,
}

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

st.markdown("""
<div class="sp-banner">
  <h1>Sistem Pakar Investasi Keuangan</h1>
  <p>
  Kelompok 9 • Universitas Sriwijaya 2026
  </p>
</div>
""", unsafe_allow_html=True)

if st.session_state.step == 0:
    st.markdown("""
<div class="sp-card">
  <div class="sp-intro-item"><span>Forward Chaining:</span><span>Inferensi maju dari fakta ke kesimpulan dengan 15 aturan IF THEN dalam 3 rule set.</span></div>
  <div class="sp-intro-item"><span>Certainty Factor:</span><span>Mengukur tingkat keyakinan rekomendasi berdasarkan kepastian pengguna dan pakar.</span></div>
  <div class="sp-intro-item"><span>Hasil:</span><span>Fokus Menabung, Risiko Rendah, Risiko Sedang, Risiko Tinggi.</span></div>
  <div class="sp-formula">CF(H,E) = CF(E) x CF(RULE) | AND: min(CF_i) x CF(RULE) | Combine: CF1 + CF2 x (1 - CF1)</div>
  <p style="font-size:15px;opacity:.75;margin-top:12px;color:#111111">Jawab 5 pertanyaan singkat. Estimasi waktu sekitar 2 menit.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
    <div class="sp-card">
    <div class="sp-section-hd">Pilihan Rekomendasi</div>

    <div class="sp-option-box option-save">
        <div class="sp-option-title">Fokus Menabung</div>
        Belum siap berinvestasi. Prioritaskan dana darurat, utang konsumtif, dan stabilitas keuangan.
    </div>

    <div class="sp-option-box option-low">
        <div class="sp-option-title">Risiko Rendah</div>
        Tabungan berjangka, deposito, reksa dana pasar uang.
    </div>

    <div class="sp-option-box option-medium">
        <div class="sp-option-title">Risiko Sedang</div>
        Reksa dana campuran, reksa dana pendapatan tetap.
    </div>

    <div class="sp-option-box option-high">
        <div class="sp-option-title">Risiko Tinggi</div>
        Saham, aset kripto.
    </div>
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1.5, 1, 1.5])

    with center:
        if st.button("Mulai Konsultasi"):
            st.session_state.step = 1
            st.rerun()

elif 1 <= st.session_state.step <= len(QUESTIONS):
    qi = st.session_state.step - 1
    q = QUESTIONS[qi]
    pct = int((qi / len(QUESTIONS)) * 100)

    st.markdown(f'<div class="sp-step-lbl">Pertanyaan {st.session_state.step} dari {len(QUESTIONS)}</div>', unsafe_allow_html=True)
    st.progress(pct)

    st.markdown(f"""
<div class="sp-card">
  <div class="sp-q-text">{q['text']}</div>
  <div class="sp-q-hint">{q['hint']}</div>
</div>
""", unsafe_allow_html=True)

    radio_left, radio_mid, radio_right = st.columns([2.4, 1.2, 2.4])
    with radio_mid:
        answer = st.radio(
            "Pilih jawaban:",
            q["options"],
            key=f"radio_{q['id']}",
            horizontal=True,
        )

    cf_key = st.select_slider(
        "Tingkat keyakinan jawaban (CF Evidence):",
        options=list(CF_OPTIONS.keys()),
        value="Yakin         (CF = 0.8)",
        key=f"cf_{q['id']}",
    )
    cf_val = CF_OPTIONS[cf_key]

    st.markdown(f"""
<div class="sp-formula">
CF(Evidence) yang dipilih = {cf_val:.1f}<br>
Rumus: CF(H,E) = CF(E) x CF(RULE) = {cf_val:.1f} x CF(RULE)
</div>
""", unsafe_allow_html=True)

    st.write("")
    btn_left, btn_gap, btn_right = st.columns([1.0, 0.6, 2.2])

    st.write("")

    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.session_state.step > 1:
            if st.button("Kembali", key="btn_back"):
                st.session_state.step -= 1
                st.rerun()

    with col3:
        label = "Lanjut" if st.session_state.step < len(QUESTIONS) else "Lihat Rekomendasi"

        if st.button(label, key="btn_next"):
            st.session_state.answers[q["id"]] = (answer, cf_val)
            st.session_state.step += 1
            st.rerun()

elif st.session_state.step == len(QUESTIONS) + 1:
    rk, rc, wm, log = run_inference(st.session_state.answers)
    rec = REC[rk]

    st.markdown(f"""
<div class="sp-res-banner" style="background:{rec['bg']}">
  <div class="sp-res-lbl">Rekomendasi Investasi Anda</div>
  <div class="sp-res-title">{rec['label']}</div>
  <div class="sp-res-inst">{rec['instrument']}</div>
</div>
""", unsafe_allow_html=True)

    if rc < 0.5:
        st.markdown(f'<div class="sp-warn">CF ({rc:.3f}) berada di bawah truthreshold 0.5. Konfirmasi ke pakar disarankan.</div>', unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=rc,
        number={"font": {"size": 38}, "valueformat": ".3f"},
        title={"text": f"Certainty Factor  <span style=\'font-size:13px;opacity:.7\'>{cf_label(rc)}</span>",
               "font": {"size": 14}},
        gauge={
            "axis": {"range": [0, 1], "tickvals": [0, 0.2, 0.4, 0.6, 0.8, 1.0]},
            "bar": {"color": "#111111"},
            "steps": [
                {"range": [0.0, 0.4], "color": "rgba(239,68,68,.15)"},
                {"range": [0.4, 0.6], "color": "rgba(234,179,8,.15)"},
                {"range": [0.6, 1.0], "color": "rgba(34,197,94,.15)"},
            ],
            "threshold": {"line": {"color": "#ef4444", "width": 3}, "thickness": 0.75, "value": 0.5},
        },
    ))
    fig.update_layout(
        height=240,
        margin=dict(t=40, b=10, l=20, r=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#111111"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="sp-section-hd">Langkah Selanjutnya</div>', unsafe_allow_html=True)
    tips_html = "".join(
        f'<div class="sp-tip"><span class="sp-tip-ck">-</span><span>{t}</span></div>'
        for t in rec["tips"]
    )
    st.markdown(f'<div class="sp-card">{tips_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sp-section-hd">Ringkasan Jawaban Anda</div>', unsafe_allow_html=True)
    user_keys = [
        ("pendapatan_stabil", "Pendapatan Stabil"),
        ("dana_darurat", "Dana Darurat"),
        ("utang_konsumtif", "Utang Konsumtif"),
        ("literasi_keuangan", "Literasi Keuangan"),
        ("toleransi_risiko", "Toleransi Risiko"),
    ]
    rows_html = ""
    for kid, klabel in user_keys:
        val, cf = wm.get(kid, ("—", 0))
        rows_html += f"""
<tr>
  <td class="sp-wm-key">{klabel}</td>
  <td class="sp-wm-val">{val}</td>
  <td class="sp-wm-cf">CF = {cf}</td>
</tr>"""
    st.markdown(f'<div class="sp-card"><table class="sp-wm-table">{rows_html}</table></div>', unsafe_allow_html=True)

    st.markdown('<div class="sp-section-hd">Working Memory</div>', unsafe_allow_html=True)
    derived_keys = [
        ("kesiapan_investasi", "Kesiapan Investasi"),
        ("profil_risiko", "Profil Risiko"),
        ("rekomendasi", "Rekomendasi"),
    ]
    rows_html2 = ""
    for kid, klabel in derived_keys:
        val, cf = wm.get(kid, ("—", 0))
        rows_html2 += f"""
<tr>
  <td class="sp-wm-key">{klabel}</td>
  <td class="sp-wm-val">{val}</td>
  <td class="sp-wm-cf">CF = {cf:.3f}</td>
</tr>"""
    st.markdown(f'<div class="sp-card"><table class="sp-wm-table">{rows_html2}</table></div>', unsafe_allow_html=True)

    with st.expander("Log Forward Chaining"):
        log_text = "\n".join(log)
        st.markdown(f'<div class="sp-log">{log_text}</div>', unsafe_allow_html=True)

    with st.expander("Referensi Formula Certainty Factor"):
        st.markdown("""
| Formula | Keterangan |
|---|---|
| `CF(H,E) = CF(E) x CF(RULE)` | Rule dengan 1 premis |
| `CF(AND) = min(CF_E1, CF_E2, ...) x CF(RULE)` | Rule dengan premis AND |
| `CF_combine = CF1 + CF2 x (1 - CF1)` | Gabung dua rule positif |
| TruthThreshold = **0.5** | Batas minimum CF untuk diterima |

**Interpretasi nilai CF:**  
CF >= 0.8 -> Almost Certainly | CF 0.6-0.8 -> Probably | CF 0.4-0.6 -> Maybe | CF < 0.4 -> Weak
""")

    left, center, right = st.columns([1.5, 1, 1.5])

    with center:
        if st.button("Konsultasi Ulang"):
            st.session_state.step = 0
            st.session_state.answers = {}
            st.rerun()