def get_profile_image_size(size):
	PROFILE_IMAGE_SIZE={
		'SM':{
			'HEIGHT':100,
			'WIDTH':100
		},
		'MID':{
			'HEIGHT':250,
			'WIDTH':250
		}
	}

	return PROFILE_IMAGE_SIZE[size]