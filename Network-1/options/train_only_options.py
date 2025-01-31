import argparse
import os.path as osp
class TrainOptions():
    def initialize(self):
        parser = argparse.ArgumentParser(description="adaptive segmentation netowork")
        parser.add_argument("--model", type=str, default='DeepLab',help="available options : DeepLab and VGG")
        parser.add_argument("--source", type=str, default='eyes',help="source dataset : gta5 or synthia")
        parser.add_argument("--target", type=str, default='eyes',help="target dataset : cityscapes")
        parser.add_argument("--batch-size", type=int, default=1, help="input batch size.")
        parser.add_argument("--num-workers", type=int, default=4, help="number of threads.")
        parser.add_argument("--data-dir", type=str, default='/extracephonline/medai_data2/lolitazhang/my-master/eyes-master/path/to/dataset-new/source/eyesgan', help="Path to the directory containing the source dataset.")
        parser.add_argument("--data-list", type=str, default='/extracephonline/medai_data2/lolitazhang/my-master/eyes-master/path/to/dataset-new/source.txt', help="Path to the file listing the images in the source dataset.")
        parser.add_argument("--data-dir-target", type=str, default='/extracephonline/medai_data2/lolitazhang/my-master/eyes-master/path/to/dataset-new/target', help="Path to the directory containing the target dataset.")
        parser.add_argument("--data-list-target", type=str, default='/extracephonline/medai_data2/lolitazhang/my-master/eyes-master/path/to/dataset-new/target.txt', help="Path to the file listing the images in the target dataset.")
        #parser.add_argument("--data-label-folder-target", type=str, default='pseudo_label_folder_name', help="Path to the soft assignments in the target dataset.")    
        parser.add_argument("--data-label-folder-target", type=str, default=None, help="Path to the soft assignments in the target dataset.")
        parser.add_argument("--learning-rate", type=float, default=2.5e-4, help="initial learning rate for the segmentation network.")
        parser.add_argument("--learning-rate-D", type=float, default=1e-4, help="initial learning rate for discriminator.")
        parser.add_argument("--lambda-adv-target", type=float, default=0.001, help="lambda_adv for adversarial training.")
        parser.add_argument("--momentum", type=float, default=0.9, help="Momentum component of the optimiser.")
        parser.add_argument("--num-classes", type=int, default=3, help="Number of classes for cityscapes.")
        parser.add_argument("--num-steps", type=int, default=250000, help="Number of training steps.")
        parser.add_argument("--num-steps-stop", type=int, default=50000, help="Number of training steps for early stopping.")
        parser.add_argument("--power", type=float, default=0.9, help="Decay parameter to compute the learning rate (only for deeplab).")
        parser.add_argument("--init-weights", type=str, default='/extracephonline/medai_data2/lolitazhang/my-master/eyes-master/path/to/initial_weights/DeepLab_init.pth', help="initial model.")
        #parser.add_argument("--restore-from", type=str, default='../path/to/snapshots/level_0.5-0.7/eyes_noise_ssl_0.9/eyes_2000', help="Where restore model parameters from.")
        parser.add_argument("--restore-from", type=str, default=None, help="Where restore model parameters from.")
        parser.add_argument("--print-freq", type=int, default=1, help="print loss and time fequency.")
        #parser.add_argument("--snapshot-dir", type=str, default='../path/to/snapshots/level_0.5-0.7/eyes_noise_ssl_0.9', help="Where to save snapshots of the model.")
        parser.add_argument("--snapshot-dir", type=str, default='../path/to/snapshots/clean', help="Where to save snapshots of the model.")
        parser.add_argument("--weight-decay", type=float, default=0.0005, help="Regularisation parameter for L2-loss.")
        parser.add_argument("--set", type=str, default='train', help="choose adaptation set.")  
        parser.add_argument("--save-pred-every", type=int, default=5000, help="Save summaries and checkpoint every often.")
        #parser.add_argument('--load_selected_samples', type=str, default='../pOSAL-master-noise/data/refuge-new/source/disc_small/level_0.2-0.3/noise_mask_0.1/selected_sample1.txt')
        parser.add_argument('--load_selected_samples', type=str, help='dir to load selected samples', default=None)
        parser.add_argument('--save_selected_samples', type=str, default=None)
        #parser.add_argument('--save_selected_samples', type=str, default='../path/to/dataset-new/source/eyesgan/level_0.2-0.3/noise_labels_0.9/selected_sample2.txt')
        parser.add_argument('--remember_rate', type=float, help='remember_rate ', default=0.1)
        parser.add_argument('--total_number', type=int, help='total number ', default=400)
        return parser.parse_args()
    
    def print_options(self, args):
        message = ''
        message += '----------------- Options ---------------\n'
        for k, v in sorted(vars(args).items()):
            comment = ''
            message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
        message += '----------------- End -------------------'
        print(message)
    
        # save to the disk
        file_name = osp.join(args.snapshot_dir, 'opt.txt')
        with open(file_name, 'wt') as args_file:
            args_file.write(message)
            args_file.write('\n')    
        
