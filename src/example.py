from wsi_registration import TissueDetector, MatcherParameters, WSI_Matcher
fixed_wsi = "./HE_99E1_p3_cropped.tif"  # file name of your fixed (template) whole slide image
float_wsi = "./HE_99E1_p3_cropped_TEMPLATE.tif"  # file name of your float (moving) whole slide image
# define the tissue detector, so the patches can be sampled
tissue_detector = TissueDetector("LAB_Threshold", threshold=80) # option 1
# tissue_detector = TissueDetector("GNB", threshold=0.5)    # option 2
matcher_parameters = MatcherParameters()  # use the default parameters
matcher = WSI_Matcher(tissue_detector, matcher_parameters)
offset = matcher.match(fixed_wsi, float_wsi)
print("Shifting offset: %d %d" % offset)


