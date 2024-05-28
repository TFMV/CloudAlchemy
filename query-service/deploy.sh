gcloud builds submit --tag gcr.io/tfmv-371720/query-service:latest

gcloud run deploy query-service \
    --image gcr.io/tfmv-371720/query-service:latest \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 4Gi \
    --timeout 3600 \
    --cpu 4 \
    --min-instances 1 \
    --service-account=sa-api@tfmv-371720.iam.gserviceaccount.com