/**
 * Enhanced Form Accessibility and Validation
 * Provides real-time validation feedback and accessibility improvements
 */

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form[aria-labelledby="form-heading"]');
    if (!form) return;

    // Real-time validation for form fields
    const fields = form.querySelectorAll('input, textarea, select');

    fields.forEach(field => {
        // Add real-time validation
        field.addEventListener('blur', validateField);
        field.addEventListener('input', debounce(validateFieldRealTime, 500));

        // Enhanced keyboard navigation
        field.addEventListener('keydown', handleKeyboardNavigation);

        // Announce changes to screen readers
        field.addEventListener('focus', announceFieldInstructions);
    });

    // Form submission handling
    form.addEventListener('submit', handleFormSubmit);

    /**
     * Validate individual field on blur
     */
    function validateField(event) {
        const field = event.target;
        const fieldContainer = field.closest('.form-control');
        const errorContainer = document.getElementById(`${field.id}-error`);

        // Clear previous validation state
        clearFieldValidation(field);

        const errors = getFieldErrors(field);

        if (errors.length > 0) {
            markFieldAsInvalid(field, errors[0]);
            announceError(field, errors[0]);
        } else {
            markFieldAsValid(field);
        }
    }

    /**
     * Real-time validation while typing (debounced)
     */
    function validateFieldRealTime(event) {
        const field = event.target;

        // Only validate if field has been touched and has content
        if (field.value.length > 0) {
            const errors = getFieldErrors(field);

            if (errors.length === 0 && field.hasAttribute('aria-invalid')) {
                markFieldAsValid(field);
            }
        }
    }

    /**
     * Get validation errors for a field
     */
    function getFieldErrors(field) {
        const errors = [];
        const value = field.value.trim();
        const fieldType = field.type;
        const isRequired = field.hasAttribute('required');

        // Required field validation
        if (isRequired && !value) {
            errors.push('Dette felt er påkrævet');
        }

        // Email validation
        if (fieldType === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                errors.push('Indtast en gyldig email-adresse');
            }
        }

        // Phone validation (Danish format)
        if (fieldType === 'tel' && value) {
            const phoneRegex = /^(\+45\s?)?(\d{2}\s?\d{2}\s?\d{2}\s?\d{2}|\d{8})$/;
            if (!phoneRegex.test(value)) {
                errors.push('Indtast et gyldigt telefonnummer (f.eks. +45 12 34 56 78)');
            }
        }

        // Name validation (minimum 2 characters)
        if (field.name === 'name' && value && value.length < 2) {
            errors.push('Navn skal være mindst 2 tegn langt');
        }

        return errors;
    }

    /**
     * Mark field as invalid
     */
    function markFieldAsInvalid(field, errorMessage) {
        field.setAttribute('aria-invalid', 'true');
        field.classList.add('input-error', 'textarea-error');

        // Update or create error message
        let errorContainer = document.getElementById(`${field.id}-error`);
        if (!errorContainer) {
            errorContainer = createErrorContainer(field);
        }

        errorContainer.querySelector('.label-text-alt').textContent = errorMessage;
        errorContainer.style.display = 'block';

        // Update aria-describedby
        updateAriaDescribedBy(field);
    }

    /**
     * Mark field as valid
     */
    function markFieldAsValid(field) {
        field.setAttribute('aria-invalid', 'false');
        field.classList.remove('input-error', 'textarea-error');

        const errorContainer = document.getElementById(`${field.id}-error`);
        if (errorContainer) {
            errorContainer.style.display = 'none';
        }
    }

    /**
     * Clear field validation state
     */
    function clearFieldValidation(field) {
        field.classList.remove('input-error', 'textarea-error');
        const errorContainer = document.getElementById(`${field.id}-error`);
        if (errorContainer) {
            errorContainer.style.display = 'none';
        }
    }

    /**
     * Create error container for a field
     */
    function createErrorContainer(field) {
        const fieldContainer = field.closest('.form-control');
        const errorContainer = document.createElement('div');
        errorContainer.id = `${field.id}-error`;
        errorContainer.className = 'label';
        errorContainer.setAttribute('role', 'alert');
        errorContainer.setAttribute('aria-live', 'polite');
        errorContainer.style.display = 'none';

        const errorText = document.createElement('span');
        errorText.className = 'label-text-alt text-error';
        errorContainer.appendChild(errorText);

        fieldContainer.appendChild(errorContainer);
        return errorContainer;
    }

    /**
     * Update aria-describedby attribute
     */
    function updateAriaDescribedBy(field) {
        const describedBy = [];
        const helpContainer = document.getElementById(`${field.id}-help`);
        const errorContainer = document.getElementById(`${field.id}-error`);

        if (errorContainer && errorContainer.style.display !== 'none') {
            describedBy.push(`${field.id}-error`);
        }
        if (helpContainer) {
            describedBy.push(`${field.id}-help`);
        }

        if (describedBy.length > 0) {
            field.setAttribute('aria-describedby', describedBy.join(' '));
        } else {
            field.removeAttribute('aria-describedby');
        }
    }

    /**
     * Announce error to screen readers
     */
    function announceError(field, message) {
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'assertive');
        announcement.setAttribute('aria-atomic', 'true');
        announcement.className = 'sr-only';
        announcement.textContent = `Fejl i ${field.labels[0]?.textContent || field.name}: ${message}`;

        document.body.appendChild(announcement);

        // Remove after announcement
        setTimeout(() => {
            document.body.removeChild(announcement);
        }, 1000);
    }

    /**
     * Announce field instructions on focus
     */
    function announceFieldInstructions(event) {
        const field = event.target;
        const helpContainer = document.getElementById(`${field.id}-help`);

        if (helpContainer) {
            // Ensure help text is announced
            helpContainer.setAttribute('aria-live', 'polite');
            setTimeout(() => {
                helpContainer.removeAttribute('aria-live');
            }, 100);
        }
    }

    /**
     * Handle keyboard navigation
     */
    function handleKeyboardNavigation(event) {
        // Enter key in text inputs should not submit form
        if (event.key === 'Enter' && event.target.type !== 'submit') {
            if (event.target.tagName !== 'TEXTAREA') {
                event.preventDefault();

                // Move to next field
                const formElements = Array.from(form.querySelectorAll('input, textarea, select, button'));
                const currentIndex = formElements.indexOf(event.target);
                const nextElement = formElements[currentIndex + 1];

                if (nextElement) {
                    nextElement.focus();
                }
            }
        }
    }

    /**
     * Handle form submission
     */
    function handleFormSubmit(event) {
        // Validate all fields before submission
        let hasErrors = false;
        const submitButton = form.querySelector('button[type="submit"]');

        // Show loading state
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = `
                <svg class="animate-spin w-5 h-5 mr-2" fill="none" viewBox="0 0 24 24" aria-hidden="true">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Sender...
            `;
        }

        fields.forEach(field => {
            const errors = getFieldErrors(field);
            if (errors.length > 0) {
                markFieldAsInvalid(field, errors[0]);
                hasErrors = true;
            }
        });

        if (hasErrors) {
            event.preventDefault();

            // Reset submit button
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.innerHTML = `
                    <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                    </svg>
                    Send besked
                `;
            }

            // Focus first field with error
            const firstErrorField = form.querySelector('[aria-invalid="true"]');
            if (firstErrorField) {
                firstErrorField.focus();

                // Announce form has errors
                announceFormErrors();
            }
        }
    }

    /**
     * Announce form submission errors
     */
    function announceFormErrors() {
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'assertive');
        announcement.setAttribute('aria-atomic', 'true');
        announcement.className = 'sr-only';
        announcement.textContent = 'Formularen indeholder fejl. Ret fejlene og prøv igen.';

        document.body.appendChild(announcement);

        setTimeout(() => {
            document.body.removeChild(announcement);
        }, 3000);
    }

    /**
     * Debounce utility function
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Initialize form state
    fields.forEach(field => {
        field.setAttribute('aria-invalid', 'false');
        updateAriaDescribedBy(field);
    });

    // Enhanced focus management for form
    const firstField = form.querySelector('input, textarea, select');
    if (firstField && document.activeElement === document.body) {
        // Only focus if no other element has focus
        firstField.focus();
    }
});