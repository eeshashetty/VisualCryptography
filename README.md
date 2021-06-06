# VisualCryptography

Copyright Authentication System via Watermarking Images, uses Visual Cryptography.

Original Code https://github.com/Shikhar0051/Visual-Cryptography-for-Copyright-Protection

## Steps

1. Generate Ownership Share for the Original Image
```bash
python3 ownership_gen.py --image IMAGE_PATH --watermark WATERMARK_PATH
```
2. To Check Authenticity for Similar Images, run `check_auth` with the Ownership Share created in Step 1
```bash
python3 check_auth.py --image IMAGE_PATH --owner OWNERSHIPSHARE_PATH --watermark WATERMARK_PATH
```

If similarity level is more than 80%, the Image is authentic. Otherwise, it's fake.


