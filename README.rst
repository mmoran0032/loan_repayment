Loan Repayment
==============

Bayesian approach to determining default risk for loans, using `Lending Club`_
data from 2007-2011. Follows along with some of the `Fast Forward Labs`_ guide
to probabilistic programming, but adding in my knowledge of ``pymc3`` following
presentations and tutorials for the library.


Data
----

The loan data from Lending Club contains the current status of the loan, the
loan principle, and attributes about the loan and the person getting the loan.
We want to limit ourselves to just those attributes that could be used by the
lendee to guage their own capability in repaying the loan, and to help them
decide if the loan is right for them.

Those columns are:
-   annual_inc
-   dti
-   revol_util
-   **int_rate**: interest rate of the loan (in percent)
-   loan_amnt
-   **term**: the length of time for the loan (either 3- or 5-year terms)
-   purpose
-   loan_status
-   total_rec_prncp

.. _`Lending Club`: https://www.lendingclub.com/info/download-data.action
.. _`Fast Forward Labs`: http://www.fastforwardlabs.com
