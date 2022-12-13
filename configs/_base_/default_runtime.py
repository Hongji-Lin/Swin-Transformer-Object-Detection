checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = '/home/lhj/Documents/GitHub/Swin-Transformer-Object-Detection/weights/mask_rcnn_swin_tiny_patch4_window7.pth' # 预训练权重位置
resume_from = None
workflow = [('train', 1)]
