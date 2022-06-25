# Webhook-for-alertmanager
Simple flask application to recive notifications from prometheus alert manager on telegram and sms(via Kavenegar)

1.At first you should create your python virtual environment usuig :
    python3 -m venv .venv
    source .venv/bin/activate
    
2.Install python libraries via :
    pip install -r requrements.txt
    
3.Edit webhook.py and set your telegram_bot_token, telegram_chat_id, kavenegar_api_key, kavenegar_sender and kavenegar_receptor

4.Move webhook.service to /lib/systemd/system/ via :
    sudo mv ./webhook.service /lib/systemd/system/
    
5.Create webhook.service soft link to /etc/systemd/system/ via :
    sudo ln -s /lib/systemd/system/webhook.service /etc/systemd/system/webhook.service
    
6.Load new services in systemd :
    sudo systemctl daemon-reload
    
7.Start and enable webhook service :
    sudo systemctl start webhook.service
    sudo systemctl enable webhook.service
    
8.Enjoy it
