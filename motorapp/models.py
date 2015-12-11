from django.db import models

class Dataset(models.Model):
    """
    :param raw_data: data set (nb_sample, nb_raw_features)
    :param description: problem description

    :type raw_data: FileField, max_length=200, null=True, blank=True
    :type description: CharField, max_length=300, null=True, blank=True
    """
    raw_data = models.FileField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    def __unicode__(self):
        return self.description

class Problem(models.Model):
    """Class about the problem table

    :param dataset: associated dataset
    :param pb_type: problem type, can be classification or regression (a a start)
    :param cost_function: cost function to minimize
    :param target: target data set (nb_sample, nb_target_dim)
    :param description: problem description
    :param train_prop: proportion of training dataset

    :type dataset: ForeignKey(Dataset), max_length=200, null=True, blank=True
    :type pb_type: CharField, choices (CLF or REG), max_length=3, null=True, blank=True
    :type cost_function: CharField, max_length=200, null=True, blank=True
    :type target: FileField, max_length=200, null=True, blank=True
    :type description: CharField, max_length=300, null=True, blank=True
    :type train_prop: IntegerField, default=68, null=True, blank=True
    """
    dataset = models.ForeignKey(Dataset, null=True, blank=True)
    PB_CHOICES = (
        ('CLF', 'classification'),
        ('REG', 'regression'),
    )
    pb_type = models.CharField(max_length=3, choices=PB_CHOICES, null=True, blank=True)
    cost_function = models.CharField(max_length=200, null=True, blank=True)
    target = models.FileField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    train_prop = models.IntegerField(default=68, null=True, blank=True)
    def __unicode__(self):
        return self.description

class Features(models.Model):
    """Class about the feature table

    :param data: features (nb_sample, nb_features)
    :param problem: associated problem
    :param description: features description

    :type data: FileField, max_length=200, null=True, blank=True
    :type problem: ForeignKey(Problem), null=True, blank=True
    :type description: CharField, max_length=300, null=True, blank=True
    """
    data = models.FileField(max_length=200, null=True, blank=True)
    problem = models.ForeignKey(Problem, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    def __unicode__(self):
        return self.description

class Estimator(models.Model):
    """Class about the estimator

    :param name: Estimator's name
    :param data: Estimator's name
    :param dict_param: dictionnary containing estimator parameters
    :param dict_perf: dictionnary containing estimator pierformances

    :type name: CharField, max_length=20, null+True, blank=True
    :type name: CharField, max_length=20, null+True, blank=True
    :type dict_param: FileField, max_length=200, null=True, blank=True
    :type dict_perf: FileField, max_length=200, null=True, blank=True
    """
    name = models.CharField(max_length=20, null=True, blank=True)
    data = models.ForeignKey(Features, null=True, blank=True)
    dict_param = models.FileField(max_length=200, null=True, blank=True)
    dict_score = models.FileField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.name

