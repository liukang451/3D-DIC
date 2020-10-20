import muDIC as dic

def Step2():

    path = input("Enter image folder:")

    # Examples:
    # ./test_imgs/speckle objects/ , png
    # ./Examples/example_data/ , tif

    file_type = input("Enter image file type:")
    image_stack = dic.image_stack_from_folder(path,file_type="."+file_type)
    mesher = dic.Mesher()
    mesh = mesher.mesh(image_stack)

    inputs = dic.DICInput(mesh, image_stack)
    dic_job = dic.DICAnalysis(inputs)
    dic_output = dic_job.run()

    # 2D DIC result visualization
    fields = dic.Fields(dic_output,upscale=10)
    viz = dic.Visualizer(fields,images=image_stack)
    viz.show(field="displacement", component=(1, 1), frame=1)

    '''
     field : string
            The name of the field to be shown. Valid inputs are:
                "true strain"
                "eng strain"
                "disp"
                "green strain"
                "residual"
    '''
    # Extract points' coordinates from output
    Points_1 = []
    Points_2 = []
    for i in range(len(dic_output.xnodesT)):
        Points_1.append([dic_output.xnodesT[i][0], dic_output.ynodesT[i][0]])
        Points_2.append([dic_output.xnodesT[i][1], dic_output.ynodesT[i][1]])

    result = [Points_1, Points_2]

    return result

