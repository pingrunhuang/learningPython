districts = ["东城区", "朝阳区", "海淀区", "西城区", "丰台区"]

def process(district):
    for _ in range(100):
        print("Processing ", district)
    
if __name__ == "__main__":
    from multiprocessing.pool import Pool
    num_of_process = 3
    p = Pool(processes=num_of_process)
    results = p.map(process, districts)