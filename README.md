# PlanarRF 

see the [TASK.md file for a description of PlanarRF](TASK.md)

## Test

Execute 
`python3 -m unittest ` to run the unit tests.

## Deploy

To deploy this as a Google Cloud Function execute:
``` 
gcloud functions deploy ncstp_best_station --entry-point best_station --runtime python37 --trigger-http --allow-unauthenticated1
```

Call the resulting URL for a point - ex. (18,18) - like this: 
```
curl -v 'URL?x=18&y=18'
```
