# Jirani-Farm

A web platform for linking farmers to tractors in their area for lease.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following to get started:

* Python 3.6 or higher
* Django 2.2 or higher
* PostgreSQL 9.6 or higher

### Installation

To install the project, clone the repository to your local machine:

```
git clone https://github.com/yourusername/jirani-farm.git
```

Then, create a virtual environment and install the dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup

Once the dependencies are installed, you need to create a database and a superuser account. To do this, run the following commands:

```
python manage.py migrate
python manage.py createsuperuser
```

### Running the Project

To run the project, run the following command:

```
python manage.py runserver
```

The project will be available at http://localhost:8000.

## Usage

The project is a web platform for linking farmers to tractors in their area for lease. Farmers can create a profile and list their tractors for lease. Tractor owners can search for tractors in their area and contact the farmers to arrange a lease.

The project includes the following features:

* User registration and login
* Tractor listing
* Tractor search
* Tractor rental

## Contributing

Contributions are welcome! Please see the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

The project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.