<div x-data="{ isOpen: @entangle('isOpen') }" class="relative">
    <!-- Botón para abrir/cerrar el dropdown -->
    <button @click="isOpen = !isOpen" class="bg-gray-700 text-white font-semibold py-2 px-4 rounded-lg shadow-md transition duration-300 ease-in-out">
        ⚙️ Settings
    </button>

    <!-- Dropdown menu -->
    <div x-show="isOpen" x-on:click.away="isOpen = false" class="absolute left-0 mt-2 w-40 bg-white dark:bg-gray-700 rounded-lg shadow-lg z-50">
        <ul class="text-sm text-gray-700 dark:text-gray-300 w-full">
            <li>
                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600">✏️ Edit</a>
            </li>
            <li class="flex justify-center items-center">
                <button wire:click.prevent="deleteProject({{ $project->id }})" class="block px-12 py-2 hover:bg-gray-100 dark:hover:bg-gray-600">🗑️ Delete</button>
            </li>
        </ul>
    </div>
</div>
