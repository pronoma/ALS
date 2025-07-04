### Analysis and Experimentation with the Annealed Langevin Sampling algorithm by Song, Ermon, 2020.

Implementation details: 

 Please install the codebase for ncsnv2 from https://github.com/pronoma/ALS, download the dataset from https://drive.google.com/drive/folders/1KM8rvaNB1DAMqwxipK75J7kR1Coq0U9r and add it to the exp/datasets folder. Install python 3.9, and create a new python virtual environment using: python3 -m venv myenv where venv is your virtual environment. Activate your environment using the command: myenv/bin/activate. After this install all necessary packages provided in the requirement.txt file using: pip install -r requirement.txt.
- Each dataset has a config file, for our dataset FFHQ the config file is the ffhq.yml. For changing the initial noise level, final noise level and number of noise levels: please change the parameters sigma_begin, sigma_end, num_classes. 
-For training, please run python main.py --config ffhq.yml --doc ffhq
- For sampling from a pretrained checkpoint or after training after n_epochs, change the checkpt_id to n_epochs, and run python main.py --sample --config ffhq.yml -i ffhq --doc ffhq
- Your samples will be saved in exp/image_samples. You will get a grid of size batch_size specified in the config file under sampling.
- Depending on the number of GPUS in your system, you can take num_workers = number of gpus
- After completing your experiments, you can deactivate your virtual environment by typing deactivate

Some experiments performed by me and their results are in these slides: https://docs.google.com/presentation/d/1IHWp4SXvpobIJEpiJEBnlFwEKCPsC8xF9CVrADPPPTA/edit?usp=sharing
