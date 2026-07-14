# Laman Rasmi Program — PKD Bachok '26

Halaman perantara untuk perkongsian melalui WhatsApp bagi:

**Jelajah Larian Obor Kesihatan Mental & Sambutan Hari Pencegahan Bunuh Diri, Peringkat Negeri Kelantan 2026**

Apabila pautan GitHub Pages ditekan, pelayar akan terus membuka:

https://sites.google.com/moh.gov.my/pkdbachoklarianobor26/laman-rasmi-program

## Cara menerbitkan di GitHub Pages

1. Cipta repository baharu bernama `pkdbachok-larian-obor-2026`.
2. Pilih **Public** dan tekan **Create repository**.
3. Muat naik semua fail dalam folder ini ke bahagian utama repository. Jangan tambah fail `.nojekyll` kerana halaman menggunakan GitHub Pages untuk membina URL imej pratonton secara automatik.
4. Buka **Settings → Pages**.
5. Di bawah **Build and deployment**, pilih:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/ (root)`
6. Tekan **Save**.

Pautan perkongsian anda akan berbentuk:

`https://NAMA-PENGGUNA-GITHUB.github.io/pkdbachok-larian-obor-2026/`

## Kandungan pratonton WhatsApp

**Tajuk**

Jelajah Larian Obor Kesihatan Mental & Sambutan Hari Pencegahan Bunuh Diri, Peringkat Negeri Kelantan 2026

**Keterangan**

Laman Rasmi Program

**Imej**

`og-preview.jpg` — 1200 × 630 piksel.

## Catatan

WhatsApp kadangkala menyimpan pratonton lama dalam cache. Selepas mengubah fail, uji semula menggunakan pautan dengan parameter sementara, contohnya:

`https://NAMA-PENGGUNA-GITHUB.github.io/pkdbachok-larian-obor-2026/?v=2`


## URL imej pratonton

Kod menggunakan `{{ site.github.url }}` supaya GitHub Pages menghasilkan URL mutlak untuk `og-preview.jpg` secara automatik. Ini membantu WhatsApp mengambil imej pratonton daripada alamat repository sebenar tanpa anda perlu menaip nama pengguna GitHub dalam kod.

## Menjana semula imej pratonton

Fail `generate_preview.py` disertakan. Frasa **“Sambutan Hari Pencegahan Bunuh Diri”** ditetapkan dalam warna jingga yang sama supaya dibaca sebagai satu komponen program.
