# Webhook-for-alertmanager
Simple flask application to recive notifications from prometheus alert manager on telegram and sms(via Kavenegar)

# Create your python virtual environment usuig :
```
python3 -m venv .venv
source .venv/bin/activate
```
# Install python libraries via :
```
pip install -r requrements.txt
```    
* Edit webhook.py and set your telegram_bot_token, telegram_chat_id, kavenegar_api_key, kavenegar_sender and kavenegar_receptor

# Move webhook.service to /lib/systemd/system/ via :
```
sudo mv ./webhook.service /lib/systemd/system/
```    
# Create webhook.service soft link to /etc/systemd/system/ via :
```
sudo ln -s /lib/systemd/system/webhook.service /etc/systemd/system/webhook.service
```    
# Load new services in systemd :
```
sudo systemctl daemon-reload
``` 
# Start and enable webhook service :
```
sudo systemctl start webhook.service
sudo systemctl enable webhook.service
```    
# Enjoy it ;)
