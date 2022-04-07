let timeOption = ['1400','1430','1500','1530','1600','1630','1700','1730','1800','1830','1900','1930','2000','2030','2100','2130','2200','2230','2300']
let sizeOption = ['1', '2', '3', '4', '5', '6', '7', '7', '8', '9', '10']

export let bookingFormValidator = {
    name: {
        length: {
            minimum: 4,
            maximum: 50,
            message: 'Your name must be between 4 and 50 characters'
        },

    },
    email: {
        length: {
            maximum: 200,
            message: 'Email can\'t exceed 200 characters'
        },
        email: {
            message: 'Invalid email format'
        }
    },
    bookingTime: {
        inclusion: {
            within: timeOption,
            message: 'Invalid booking time'
        }
    },
    bookingSize: {
        inclusion: {
            within: sizeOption,
            message: 'Invalid booking size'
        }
    }
}