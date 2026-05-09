# Workflow CI - MLProject

Folder ini berisi konfigurasi untuk Kriteria 3 (Advanced Level) yaitu membuat Workflow CI yang menjalankan eksperimen `mlflow run` dan melakukan build serta push image Docker ke Docker Hub.

## Struktur Direktori
```
Workflow-CI
├── .github
│   └── workflows
│       └── ci-modelling.yml
├── MLProject
│   ├── MLproject
│   ├── conda.yaml
│   ├── modelling.py
│   ├── requirements.txt
│   └── titanic_preprocessing/
├── README.md
└── dockerhub-link.txt
```

## Persiapan untuk GitHub Actions

Untuk menjalankan CI ini dengan sukses di GitHub Actions, Anda harus mengatur repository secrets:

1. Pergi ke halaman repository GitHub Anda.
2. Klik **Settings** -> **Secrets and variables** -> **Actions**.
3. Klik **New repository secret** dan tambahkan dua variabel berikut:
   - `DOCKER_USERNAME`: Username akun Docker Hub Anda.
   - `DOCKER_PASSWORD`: Password atau Personal Access Token (PAT) Docker Hub Anda.

## Cara Kerja

Setiap kali Anda melakukan *push* perubahan ke dalam folder `MLProject/` di branch `main`:
1. GitHub Actions akan otomatis mengunduh dependency dan environment via `conda`/`pip`.
2. Menjalankan `mlflow run ./MLProject`.
3. Membangun image Docker model hasil pelatihan via `mlflow models build-docker`.
4. Mendorong (push) image Docker tersebut ke Docker Hub.

Trigger Workflow CI Action
