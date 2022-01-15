# @time 2021/10/21 13:48
# @Author howell
# @File test1.PY
from jinja2 import *

loader = """
    
        def {{methed}}(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {{data}}
        p = self.worker.post("{{methed}}", **temp_data)
        return p
        
    """
env = Environment(loader=loader, trim_blocks=False, lstrip_blocks=False)
print(env.loader)
print(env.block_start_string)

if __name__ == '__main__':
    pass
